# bpy.types.PreferencesSystem: vbo_collection_rate, vbo_time_out

vbo_collection_rate

Seconds between successive runs of the GL vertex buffer object garbage collector (in [1, 3600], default 60)

Type :

int
vbo_time_out

Seconds a GL vertex buffer object may go untouched before it is freed (use 0 to keep the VBO allocated) (in [0, 3600], default 120)

Type :

int

[Related references](INDEX.md).
