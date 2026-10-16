# Cache

### Cache 

Reference

Panel :

Particle System ‣ Cache

Real-time responsiveness improves and unnecessary recalculation reduces when particle information gets cached in memory or persisted to disk.

Emitter particle systems employ a shared caching and baking mechanism (alongside Soft Body and Cloth).

Particles Cache settings. 

See also

General Baking documentation contains supplementary details.

### Hints 

- Simulation computes exclusively for positive frame numbers within the Cache panel's Start and End boundaries, baked or not. Extending the End frame becomes necessary for simulations surpassing the default frame duration.

- Throughout animation playback, each physics system writes every frame to cache. Playback must commence before or at the simulation's start frame for cache population.

- Automatic cache clearing happens on modifications, though not universally. Manual clearing may prove necessary after force field adjustments, for instance.

- Baked systems resist post-bake alteration. Mesh changes won't retrigger simulation computation.

- The Delete Bake button in simulation cache settings clears bake results.

- Particle Edit Mode editing requires in-memory bakes only. Disk Cache prevents editing capabilities.

- Path length constraints on the blend-file location may obstruct caching, particularly when OS path length limits apply.

- Modifier stack sequencing deserves careful attention. Different face counts may appear in viewport versus render (e.g., with subdivision surface), potentially creating divergent render output.

[Related references](INDEX.md).
