# Baking Physics Simulations

## Baking Physics Simulations

Baking caches calculated simulation results to memory.

Automatic caching occurs during playback; subsequent playbacks replay from cached data faster.

Baking protects the cache; simulation settings become uneditable until cache deletion (Delete Bake).

It is recommended practice to bake physics simulations before rendering. Avoids re-simulation time; prevents glitches; ensures consistent results across renders.

Note: Most physics simulators use similar caching; not all expose identical settings. Coverage below is comprehensive; individual types may omit some options.

Options

Two simultaneous caches displayed.

Caches List
Blender manages multiple simultaneous caches for one physics object.

Rename by double-clicking. Named caches store disk files prefixed with the name (e.g., MyCache → MyCache_xxxxxx_yy.bphys). Unnamed caches use object-name-derived filenames (Cube → 43756265_xxxxxx_yy.bphys, where 43756265 encodes the object name).

Warning: Multiple caches on one object require explicit Cache Names. Unnamed-cache conflicts (same object name) cause file loss.

External
Reads cache from disk via specified path.

Note: Cache name in Caches List and Index must match external filenames (format: name_frame_index.bphys).

Index
External file index (last two digits of filename).

Path
Cache file directory.

Disk Cache
Saves simulation cache to disk (separate from blend file) in blendcache_[filename] folder.

Note: Blend file must be saved first.

Use Library Path
Share disk cache when the physics object is linked into another blend file. Enabled = linked versions share cache; disabled = independent caches.

Start
Simulation start frame.

End
Simulation end frame.

Note: Calculation occurs only for positive frames between Start and End, baked or not. Extend End frame for longer simulations.

Cache Step
Interval for storing simulation data.

Note: Some systems (particles) allow position storage at every nth frame, with interpolation between. Cache Step > 1 yields smaller files but different results.

Baking

Bake
Initiates baking (Blender freezes). Cursor shows progress. Object Mode only.

Delete Bake
Marks cache temporary: removed on next edit/frame change. (Post-bake only.)

Calculate to Frame
Bakes to current frame (End frame limit applies).

Current Cache to Bake
Converts playback cache (auto-simulated physics) to permanent. Normally erased on modification; this preserves it.

Bake All Dynamics
Bakes all scene physics (all types). Multi-physics setups.

See Bake.

Delete All Bakes
Removes all scene bakes.

See Delete Bake.

Update All to Frame
Bakes all scene physics to current frame.

See Calculate To Frame.

[Related references](INDEX.md).
