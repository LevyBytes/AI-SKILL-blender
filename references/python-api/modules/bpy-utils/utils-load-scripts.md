# bpy.utils: bpy.utils. load_scripts ( * , reload_scripts = False , refresh_scripts = False , extensions = True )

bpy.utils. load_scripts ( * , reload_scripts = False , refresh_scripts = False , extensions = True ) 

Load scripts and call each module's register function.

Parameters :

- reload_scripts ( bool ) – Makes every script run its unregister method
before being loaded again.

- refresh_scripts ( bool ) – Restricts loading to scripts that aren't yet present
as modules.

- extensions ( bool ) – Loads additional scripts (add-ons & app-templates).

[Related references](INDEX.md).
