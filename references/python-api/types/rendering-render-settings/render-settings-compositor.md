# bpy.types.RenderSettings: compositor_denoise_device, compositor_denoise_final_quality, compositor_denoise_preview_quality, compositor_device, compositor_precision

compositor_denoise_device

Which device runs the compositor's denoise nodes (default 'AUTO' )

- AUTO
Auto – Match whatever device the compositor itself is already using for the denoise node.

- CPU
CPU – Run the denoise node on the CPU.

- GPU
GPU – Run the denoise node on the GPU when one is present, otherwise drop back to the CPU.

Type :

Literal[‘AUTO’, ‘CPU’, ‘GPU’]
compositor_denoise_final_quality

Quality denoise nodes apply when final renders are composited, used whenever a node's quality option is left on Follow Scene (default 'HIGH' )

- HIGH
High – High quality.

- BALANCED
Balanced – A trade-off that sits between speed and quality.

- FAST
Fast – High performance.

Type :

Literal[‘HIGH’, ‘BALANCED’, ‘FAST’]
compositor_denoise_preview_quality

Quality denoise nodes apply for viewport and interactive compositing, used whenever a node's quality option is left on Follow Scene (default 'BALANCED' )

- HIGH
High – High quality.

- BALANCED
Balanced – A trade-off that sits between speed and quality.

- FAST
Fast – High performance.

Type :

Literal[‘HIGH’, ‘BALANCED’, ‘FAST’]
compositor_device

Chooses where the compositing runs (default 'CPU' )

Type :

Literal[‘CPU’, ‘GPU’]
compositor_precision

Numeric precision held by intermediate compositor results (default 'AUTO' )

- AUTO
Auto – Full precision on final renders, half precision the rest of the time.

- FULL
Full – Full precision.

Type :

Literal[‘AUTO’, ‘FULL’]

[Related references](INDEX.md).
