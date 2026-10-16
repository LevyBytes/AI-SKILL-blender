# bpy.types.Itasc: reiteration_method

reiteration_method

Sets whether the solver may reiterate (converge to the precision target) on no frames, only the first, or all of them (default 'NEVER' )

- NEVER
Never – The solver does not reiterate, not even on first frame (starts from rest pose).

- INITIAL
Initial – The solver reiterates (converges) on the first frame but not on subsequent frame.

- ALWAYS
Always – The solver reiterates (converges) on all frames.

Type :

Literal[‘NEVER’, ‘INITIAL’, ‘ALWAYS’]

[Related references](INDEX.md).
