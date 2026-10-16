# bpy.app.translations: bpy.app.translations. register ( module_name , translations_dict )

bpy.app.translations. register ( module_name , translations_dict )

Enroll an add-on's user-interface translations into the system.

Note

Has no effect when Blender lacks i18n support.

Parameters :

- module_name ( str ) – Identifier for the add-on.

- translations_dict ( dict [ str , dict [ tuple [ str , str ] , str ] ] ) – A dictionary organized like this:
{locale: {msg_key: msg_translation, ...}, ...}

[Related references](INDEX.md).
