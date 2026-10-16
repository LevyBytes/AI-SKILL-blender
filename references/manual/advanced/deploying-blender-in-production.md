# Deploying Blender in Production

## Deploying Blender in Production

Deploying Blender in production (studios, schools): such environments often have particular needs around security, automated deployment, and customization. Installing: a Blender download extracts to any directory as a self-contained install, several versions can coexist on one machine, and rollout can be automated with ordinary file tools. Because new versions may add, drop, or change behavior that affects production files, it's wise to pin one LTS version per project (LTS releases get two years of bug fixes). Working offline: a workstation may lack internet for security or other reasons. Blender doesn't reach the internet by default, but the System preferences' Online Access option enables it; you can enforce offline operation with the --offline-mode argument, after which users can't turn online access back on in the preferences. (Add-ons that respect this setting only connect when enabled, but Blender can't stop a third-party add-on from breaking the rule.) Bundling extensions: to hand the same extensions to everyone offline or in a controlled setup, use the default read-only System repository, which can live on a read-only network drive or a system directory. The $`BLENDER_SYSTEM_EXTENSIONS` environment variable sets its default location — point it at a directory that contains a "system" subdirectory — and extract extension packages into that system directory, giving a path like `$BLENDER_SYSTEM_EXTENSIONS/system/my-addon/blender_manifest.toml`; in the Extensions preferences you can also set a custom directory for the default System repository or create several repositories. Bundling scripts: beyond extensions, you can bundle scripts for presets, application templates, legacy add-ons, and startup. Add script directories in the File Paths preferences, or use $`BLENDER_SYSTEM_SCRIPTS` to add them without touching the preferences; a script directory is expected to hold specific subdirectories (presets, addons, startup, etc.) per the Path Layout. Startup scripts: the Python API can customize Blender — adjusting preferences, the startup file, and UI — for instance enabling an add-on for everyone via `$BLENDER_SYSTEM_SCRIPTS/startup/enable_addons.py`:
```python
def register():
    import addon_utils
    addon_utils.enable("my-addon")

def unregister():
    pass

if __name__ == "__main__":
    register()
```
Application templates set Blender up for a task or project apart from the default config (chosen when creating a file), placed like `$BLENDER_SYSTEM_SCRIPTS/startup/bl_app_templates_system/MyTemplate/__init__.py` and `.../MyTemplate/startup.blend`. Legacy add-ons not yet converted to extensions go in the addons script directory, e.g. `$BLENDER_SYSTEM_SCRIPTS/addons/simple_addon.py` or `.../addons/complex_addon/__init__.py`. Splash screen: to show which build artists are running, `BLENDER_CUSTOM_SPLASH` swaps out the entire splash image, whereas `BLENDER_CUSTOM_SPLASH_BANNER` merely lays a banner over it. VFX Platform: Blender follows the VFX reference platform, so it runs alongside other VFX tools and can trade image, volume, and scene files back and forth with them. Python version: Blender and the bpy module bind to a single Python version (so add-ons and VFX tools need only target one); Blender bundles its own complete Python and ignores the system Python by default, which --python-use-system-env can change if you set up a compatible version.

[Related references](INDEX.md).
