# gpu.types.GPUFrameBuffer: overview

class gpu.types. GPUFrameBuffer ( * , depth_slot = None , color_slots = None )

This object opens up the framebuffer functionality.
Supplying a ‘layer’ in an argument attaches a single layer of a 3D or array texture to the frame-buffer.
With cube map textures, the layer maps onto a cube map face.

Parameters :

- depth_slot (gpu.types.GPUTexture | dict[str, int | gpu.types.GPUTexture] | None) – GPUTexture to attach or a dict containing keywords: ‘texture’, ‘layer’ and ‘mip’.

- color_slots (gpu.types.GPUTexture | dict[str, int | gpu.types.GPUTexture] | Sequence[gpu.types.GPUTexture | dict[str, int | gpu.types.GPUTexture]] | None) – Tuple where each item can be a GPUTexture or a dict containing keywords: ‘texture’, ‘layer’ and ‘mip’.

[Related references](INDEX.md).
