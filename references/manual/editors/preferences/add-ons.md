# Add-ons

## Add-ons

The Add-ons section manages secondary scripts — "Add-ons" — that extend Blender's functionality; most of the time you get them through the Extensions system. Here you can search for, install, enable, and disable Add-ons. Tip: if an Add-on doesn't activate when enabled, check the Console window for any errors.

Filtering Add-ons:
Search Add-ons: Blender ships with some Add-ons preinstalled and ready to enable, but you can add your own or any interesting ones from the web.
Enabled Add-ons Only: shows only the enabled add-ons in the current Category.
Add-on Tags: add-ons are tagged by which areas of Blender they affect.

Add-on Settings:
Refresh Local: rescans extension and legacy add-ons for changes to modules and metadata (much like a restart); any issues come back as warnings.
Install from Disk — installs an extension from a .zip package into a Local Repository, with no updates available. It also installs legacy Add-ons — see Installing Legacy Add-ons.

Enabling & Disabling Add-ons: check or uncheck the box to the right of an add-on; its functionality should be available right away.

Add-on Information: click the arrow at the left of an add-on's box for more, such as its location, a description, a documentation link, and a button to report a bug specific to it.
Add-on Preferences — some add-ons carry their own preferences in the Preferences part of the add-on's information box, used for instance to enable/disable certain functions, which sometimes all default to off — so check whether an enabled add-on has any.

Installing Legacy Add-ons: click Install from Disk and pick the add-on's .py file (if it's a single file) or its .zip. The add-on isn't enabled automatically after installation; tick its checkbox to do that.
Refresh: scans the Add-on Directory for new add-ons.
Tip: this screen won't install a folder-based addon made of loose .py files, but you can still do it by adding a Script Directory:
- Create an empty directory somewhere (e.g. my_scripts).
- Add a subdirectory under my_scripts named addons (Blender requires exactly this name).
- Put your addon folder inside that addons folder.
- Open the Preferences' File Paths section.
- Add a Script Directories entry pointing at your script folder (e.g. my_scripts).
- Save the preferences and restart Blender so it picks up the new add-on location.
The add-ons in that folder then become available automatically; you just enable them.

[Related references](INDEX.md).
