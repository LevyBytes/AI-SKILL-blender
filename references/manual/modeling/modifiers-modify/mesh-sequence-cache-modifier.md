# Mesh Sequence Cache Modifier

## Mesh Sequence Cache Modifier

### Mesh Sequence Cache Modifier

Data from Alembic and USD files is what the Mesh Sequence Cache modifier reads in. It will take static meshes, but loading animated ones is its principal purpose. Its name aside, the modifier copes with curves too, and it deals with file sequences as well as with meshes and curves whose topology shifts (the output of fluid simulations, for example).

Bring in an Alembic or USD file and Mesh Sequence Cache modifiers attach themselves automatically to any time-varying meshes. Where it's the object transform that varies over time (animated rotation, location, or scale), the Transform Cache Constraint takes care of that instead. Anything that isn't Alembic or USD, MDD and PC2 among them, comes in through the Mesh Cache modifier instead.

### Options

Cache File
Data-block menu for picking the Alembic or USD file.

File Path
Where the Alembic or USD file is located.

Object Path
The route to the Alembic or USD object held inside the archive or stage.

Read Data
Sets which mesh data is brought in from the cache file.
You can switch each of the following on or off as you like:

Vertices :

Reads vertex positions and (if animated) deformations for each frame.

Faces :

Brings in the mesh's face topology and structure.

UV :

Pulls UVs (texture coordinates) out of the cache file.

Color :

Brings in vertex color attributes from the cache file when they're present.

Attributes :

Pulls in custom attributes (creases, custom normals, or generic attributes, for example).

### Time

Sequence
Whether the cache is split across a run of files or not.

Override Frame
Whether a custom frame is used to look up data in the cache file
in place of the current scene frame.

The Frame value is the time used to look up data in the cache file,
or to settle which file to use in a sequence.

Frame Offset
Taken off the current frame when looking up data in the cache file,
or when settling which file to use in a sequence.

### Velocity

Velocity Attribute
Names the Alembic attribute that feeds motion blur generation;
this defaults to .velocities , the standard across most Alembic files.

Note

For now, Velocity Attribute applies to Alembic files alone.

Velocity Unit
Sets how the velocity vectors are read with respect to time.

Frame :

The velocity unit was set in frames, so no scaling by scene FPS is needed.

Second :

The velocity unit was encoded in seconds, so the scene FPS (1 / FPS) has to scale it.

Note

At present, Velocity Unit works with Alembic files only.

Velocity Scale
A multiplier for dialing the velocity vector's magnitude up or down, feeding time effects like motion blur.

Note

Right now, Velocity Scale is limited to Alembic files.

[Related references](INDEX.md).
