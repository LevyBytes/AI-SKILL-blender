# bpy.types.FCurve: convert_to_samples, convert_to_keyframes

convert_to_samples ( start , end )

Turn this FCurve's keyframes into sample points where needed

Parameters :

- start ( int ) – Start Frame, (in [-1048574, 1048574])

- end ( int ) – End Frame, (in [-1048574, 1048574])
convert_to_keyframes ( start , end )

Turn this FCurve's sample points back into keyframes via linear interpolation, where needed

Parameters :

- start ( int ) – Start Frame, (in [-1048574, 1048574])

- end ( int ) – End Frame, (in [-1048574, 1048574])

[Related references](INDEX.md).
