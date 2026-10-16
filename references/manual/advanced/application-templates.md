# Application Templates

## Application Templates

Application templates let you define a reusable configuration that can replace the default one without a separate Blender install or overwriting your personal settings. Pick a template from the splash screen or the File ▸ New submenu (the menu is hidden on the splash when no templates are found); install new ones from the Blender menu, and save your preferences if you want the active template to persist across restarts. Motivation: sometimes a single script or add-on isn't enough and you don't want to ask someone to swap their preferences and startup file, install scripts, and change their keymap — templates let people switch to a customized configuration without disrupting their own settings or install, so they can build and easily distribute their own applications on top of Blender. Details: a template can supply its own startup file — the one loaded by default; preferences (only a subset is used: themes, add-ons, keymaps, and viewport lighting); splash-screen image; and Python scripts (with the same capabilities as any script, typically modifying or replacing parts of the UI, defining new menus/keymaps/tools, or pointing to a custom add-on path holding add-ons specific to the template). A template also keeps its own user configuration, so saving a startup file while using one won't overwrite your default. Directory layout: templates live in one of two spots under the scripts directory — {`BLENDER_USER_SCRIPTS`}/startup/bl_app_templates_user or {`BLENDER_SYSTEM_SCRIPTS`}/startup/bl_app_templates_system — and user configuration is stored in a subdirectory: without a template at ./config/startup.blend and ./config/userpref.blend, and with one at ./config/{`APP_TEMPLATE_ID`}/startup.blend and ./config/{`APP_TEMPLATE_ID`}/userpref.blend (see Blender's Directory Layout for script and config locations). If paths aren't being found, log Blender's path look-ups, e.g. `blender --log "bke.appdir.*" --log-level -1 --app-template my_app_template`, then check where it tries to access the template. You can also set up a launcher that opens Blender with a given template via `blender --app-template my_template`. Template contents (each file optional): startup.blend (the factory startup file), userpref.blend (the factory preferences file; when omitted, preferences are shared with the default config, and only a subset is used), splash.png (a splash override, which must be 1000x500, excluding header text), and __init__.py (a Python script that must contain register and unregister functions). The bundled startup.blend and userpref.blend count as Factory Settings and are never overwritten; the user can save their own startup/preferences while using the template (stored in their user config) only when the template includes its own userpref.blend, and the original template settings reload via Load Template Factory Settings in the file menu, much like Load Factory Settings. Template scripts: app templates use the same APIs as add-ons and other scripts; an optional __init__.py lets you change the startup or preferences without shipping a blend-file and lets you make changes dynamically (for example, checking the processor count, OS, and memory and setting values accordingly), and lets you enable add-ons tied to your template. The register function runs on activation and unregister when another template is selected; since these run once, any changes to defaults must go through a handler — the two you'll likely use are bpy.app.handlers.load_factory_preferences_post and bpy.app.handlers.load_factory_startup_post — which let you define your own "factory settings" the user can change, just as Blender has its own defaults on first launch. The page includes an example __init__.py defining such defaults:
```python
import bpy
from bpy.app.handlers import persistent

@persistent
def load_handler_for_preferences(_):
    print("Changing Preference Defaults!")
    from bpy import context
    prefs = context.preferences
    prefs.use_preferences_save = False
    kc = context.window_manager.keyconfigs["blender"]
    kc_prefs = kc.preferences
    if kc_prefs is not None:
        kc_prefs.select_mouse = 'RIGHT'
        kc_prefs.spacebar_action = 'SEARCH'
        kc_prefs.use_pie_click_drag = True
    view = prefs.view
    view.header_align = 'BOTTOM'

@persistent
def load_handler_for_startup(_):
    print("Changing Startup Defaults!")
    for mesh in bpy.data.meshes:
        for poly in mesh.polygons:
            poly.use_smooth = True
    for screen in bpy.data.screens:
        for area in screen.areas:
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.shading.type = 'MATERIAL'
                    space.shading.use_scene_lights = True

def register():
    bpy.app.handlers.load_factory_preferences_post.append(load_handler_for_preferences)
    bpy.app.handlers.load_factory_startup_post.append(load_handler_for_startup)

def unregister():
    bpy.app.handlers.load_factory_preferences_post.remove(load_handler_for_preferences)
    bpy.app.handlers.load_factory_startup_post.remove(load_handler_for_startup)
```

[Related references](INDEX.md).
