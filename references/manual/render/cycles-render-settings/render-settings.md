# Render Settings

## Render Settings

### Render Settings

Reference

Panel :

Render

Device
Selects the computational backend for Cycles rendering. Choice significantly impacts performance; GPU Compute often outperforms CPU.

CPU :

Render via the system's processor. All Cycles features work here. CPU thread allocation is configured in Performance Properties.

GPU Compute :

Render through one or more graphics processors via the compute backend and devices selected in Cycles Render Devices. Depending on the backend, simultaneous CPU and GPU operation may be possible.

For configuration, device options, and limitations, consult GPU Rendering.

Note

GPU rendering may have capability gaps relative to CPU rendering based on the backend.

See also

Denoising and Compositing have separate device selection.

Open Shading Language
Enables custom shading via OSL shader scripts. When OSL is active:

- Shader Editor lets you insert OSL shader nodes using the Script Node.

- Create shading logic impossible with standard Cycles nodes.

Constraints:

- OSL activates only on CPU or OptiX GPU backends.

- Rendering typically runs slower than native nodes due to shader compilation and interpretation.

- Certain features, like baking and selected volume shaders, may not support OSL.

[Related references](INDEX.md).
