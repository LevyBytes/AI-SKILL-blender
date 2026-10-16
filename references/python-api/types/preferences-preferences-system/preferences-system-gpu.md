# bpy.types.PreferencesSystem: gpu_backend, gpu_preferred_device, gpu_shader_workers

gpu_backend

Which GPU backend Blender uses (a restart is needed to apply changes) (default 'OPENGL' )

- OPENGL
OpenGL – Run on the OpenGL backend.

- METAL
Metal – Run on the Metal backend.

- VULKAN
Vulkan – Run on the Vulkan backend.

Type :

Literal[‘OPENGL’, ‘METAL’, ‘VULKAN’]
gpu_preferred_device

Which device detection should favor (a restart is needed to apply changes) (default 'AUTO' )

- AUTO
Auto – Detect the best GPU for Blender on its own.

Type :

Literal[‘AUTO’]
gpu_shader_workers

How many threads or subprocesses compile shaders, capped at the CPU's max threads (a restart is needed to apply changes). Raising it speeds compilation but uses more RAM. Set 0 for automatic configuration. (OpenGL only) (in [0, 32], default 0)

Type :

int

[Related references](INDEX.md).
