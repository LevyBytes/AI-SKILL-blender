# bpy.types.RenderSettings: threads, threads_mode

threads

Cap on how many CPU cores render at once, on multi-core/CPU machines (in [1, 1024], default 1)

Type :

int
threads_mode

Picks how the render thread count is decided (default 'AUTO' )

- AUTO
Auto-Detect – Derive the thread count automatically from the available CPUs.

- FIXED
Fixed – Set the thread count by hand.

Type :

Literal[‘AUTO’, ‘FIXED’]

[Related references](INDEX.md).
