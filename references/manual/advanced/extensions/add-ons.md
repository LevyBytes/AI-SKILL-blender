# Add-ons

## Add-ons

Add-ons extend Blender through Python, and most are delivered via the Extensions system. If one doesn't activate when enabled, check the Console window for errors. Internet access: an add-on that needs the internet must consult the read-only property bpy.app.online_access (governed by Preferences and overridable on the command line with --offline-mode / --online-mode), and can also check bpy.app.online_access_override to learn whether the user is even allowed to toggle Allow Online Access; an add-on that honors this only connects when enabled, though Blender can't stop third-party add-ons that ignore it. Bundle dependencies: to ship as an extension an add-on must be self-contained, carrying every dependency (notably third-party Python modules) — the options are bundling Python wheels (the recommended route), bundling other add-ons together (recommended when one add-on depends on another, taking care that both the standalone and the combined add-on check for already-registered types such as Operators and Panels, so installing them as a bundle and individually doesn't duplicate operators and panels), or Vendorize (to bundle a pure-Python dependency as a sub-module, which avoids version conflicts but takes setup per package). Local storage: an add-on must not assume its own directory is writable (it isn't for "System" repositories), and writing into it is risky because upgrading the extension wipes all its files; an add-on needing a user directory should call `extension_directory = bpy.utils.extension_path_user(__package__, path="", create=True)` (use the path argument for subdirectories), which persists across upgrades but is removed on uninstall. Legacy vs extension add-ons: since Extensions arrived in Blender 4.2 the old add-on style is deprecated; the changes are small but affect existing add-ons, and legacy add-ons stay supported (installable via the "Install legacy Add-on" button in preferences) while maintainers are urged to convert so their add-ons stay future-proof and can update through the extensions platform. Converting a legacy add-on to an extension means: writing a manifest file, deleting the bl_info block (now held in the manifest), replace module-name references with __package__, switch module imports to relative imports, pack external Python dependencies as wheels, and test thoroughly (installing from disk gets you closest to the real experience). Extensions and namespace: legacy add-ons used their module name to reach preferences, which could clash when same-named extensions from different repositories were installed, so the repository name is now part of the namespace — for example, kitsu becomes bl_ext.{repository_module_name}.kitsu, with implications for preferences and imports. User preferences and __package__: an add-on's preferences use the package name as their identifier via __package__, which was allowed but not enforced in legacy add-ons, so this can break backward compatibility:
```python
# Before:
class KitsuPreferences(bpy.types.AddonPreferences):
    bl_idname = "kitsu"
    # ... snip ...
# Access with:
addon_prefs = bpy.context.preferences.addons["kitsu"]

# Now:
class KitsuPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__
    # ... snip ...
# Access with:
addon_prefs = bpy.context.preferences.addons[__package__]
```
An add-on with sub-packages (sub-directories holding their own __init__.py) that needs this identifier must import the top-level package with a relative import — `from .. import __package__ as base_package` — then use base_package instead of __package__ (".." is relative to the package's parent; sub-sub-packages use "..." and so on). Note that __package__ varies between systems, so never hard-code it as a literal string, and extensions must not modify its value or they risk errors. Relative imports: imports of packages within the add-on module must be relative (e.g. `from . import utils` rather than `from kitsu import utils`) — a standard Python feature relevant only to multi-folder add-ons, again allowed but unenforced in legacy add-ons, so it can break backward compatibility.

[Related references](INDEX.md).
