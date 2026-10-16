# bpy.app: bpy.app. version_file

bpy.app. version_file
The Blender file version, as a tuple of 3 numbers (major, minor, file sub-version), used to save a .blend file. The last item is the file sub-version, which differs from the release micro version (the last item of the bpy.app.version tuple); the file sub-version can be incremented several times while a Blender version is in development, and this value is — and should be — used for handling compatibility changes between Blender versions.
Type: tuple[int, int, int]

[Related references](INDEX.md).
