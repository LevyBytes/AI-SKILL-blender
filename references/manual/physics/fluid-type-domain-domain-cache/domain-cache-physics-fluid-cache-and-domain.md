# Cache: Physics ‣ Fluid ‣ Cache, Domain

### Cache

Reference

Panel :

Physics ‣ Fluid ‣ Cache

Type :

Domain

The Cache panel manages fluid simulation baking and caching, storing outcomes to prevent recalculation.

Baking demands substantial processing (time). Scene-dependent; allocate adequate duration.

Modifier meshes use render settings for fluid export. Depending on config, time and memory can spike exponentially. Subdivision Surface on moving obstacles might warrant reduced subdivision to accelerate baking. With correct setup/rig, boost settings for realism.

Note

Fluid sims use proprietary cache. Other physics use General Baking.

Cache Directory
Location for baked files. Each simulation type (mesh, particles, noise) gets its subdirectory.

Frame Start
Sim first frame, first baked frame.

End
Sim last frame, last baked frame.

Note

Simulation only calculates positive frames within Start/End. Extend End frame for longer sims.

Offset
Frame shift on cache loading—not during baking.

Type
Cache baking methodology.

Replay :

Baking occurs as viewport playback happens.

Modular :

Step-by-step baking: bake tools are in individual panels (e.g., mesh baking in Mesh panel).

All :

Single-tool baking considering all settings. The tool lives in the Cache panel.

Important

"Replay" requires "Play Every Frame" Playback Sync. Use "Modular" or "All" for "Frame Dropping" or "Sync to Audio".

Resumable
Saves extra data for resuming post-pause. More drive usage; avoid on high-resolution bakes.

Bake All, Free All
With Final cache type. Bake All runs considering all settings (same as Modular, all at once). Status bar shows progress; Esc aborts. After baking, Free All clears cache. Pause/resume unavailable (only critical files save).

[Related references](INDEX.md).
