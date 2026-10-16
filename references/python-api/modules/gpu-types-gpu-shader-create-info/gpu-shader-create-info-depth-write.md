# gpu.types.GPUShaderCreateInfo: depth_write ( value )

depth_write ( value )

Declare how depth writing should behave when gl_FragDepth is altered.

GPUs often apply an optimization that runs an early depth
test ahead of the fragment shader, letting the shader work be
skipped when the fragment turns out to be occluded and thus discarded.

This optimization leaves the final image untouched, and it is generally
available as long as the fragment does not change its depth programmatically.
That said, there is a set of depth operations in the shader that
can still happen while keeping the early depth test usable.

This function adjusts the optimization's behavior so those operations
can be carried out.

Parameters :

value ( Literal [ 'UNCHANGED' , 'ANY' , 'GREATER' , 'LESS' ] ) – Depth write value.
:UNCHANGED: disables depth write in a fragment shader and execution of the fragments can be optimized away.
:ANY: enables depth write in a fragment shader for any fragments
:GREATER: enables depth write in a fragment shader for depth values that are greater than the depth value in the output buffer.
:LESS: enables depth write in a fragment shader for depth values that are less than the depth value in the output buffer.

[Related references](INDEX.md).
