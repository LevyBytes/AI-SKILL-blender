# Transform Cache Constraint

## Transform Cache Constraint

The Transform Cache constraint plays back an animation streamed from an Alembic or USD file — for example applying a baked rigid-body simulation to an object. It's added automatically when importing such a file, but applies only to whole-object transforms (location/rotation/scale); for deforming animation the Mesh Sequence Cache Modifier is used instead. Options: Cache File (a data-block menu to pick the Alembic or USD file); File Path (the path to it); Sequence (whether the cache is split into a series of files); Override Frame (use a custom frame to look up cache data instead of the current scene frame, the Frame value being the lookup time or which file in a sequence to use); Frame Offset (subtracted from the current frame for the lookup or file choice); Manual Scale (enlarge or shrink the object relative to the world origin); Velocity Attribute (the Alembic attribute used for motion-blur data, by default .velocities, standard for most Alembic files; Alembic only); Velocity Unit (how velocity vectors relate to time) — Frame (encoded in frames, no FPS scaling needed) or Second (encoded in seconds, scaled by 1/FPS) (Alembic only); Object Path (the path to the Alembic or USD object inside the archive or stage); and Influence.

[Related references](INDEX.md).
