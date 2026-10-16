# bpy.types.bpy_prop_collection: foreach_get, foreach_set

foreach_get ( attr , seq )

Quick reads of a basic-type attribute stored across a collection.

Parameters :

- attr ( str ) – Name of the item attribute to read (for example co , normal or
select ). The attribute must be a basic type (bool, int or float).

For geometry attribute types, see Attribute.data_type.

- seq ( MutableSequence [ bool | int | float ] | buffer ) – Writable sequence or buffer receiving flattened values.
For array attributes, the length must be len(collection) * array_length .

Only works for 'basic type' properties (bool, int and float)!
Multi-dimensional arrays (like array of vectors) will be flattened into seq.

```python
import bpy

mesh = bpy.context.object.data
collection = mesh.vertices

### Allocate a flat list for the `co` property (X, Y, Z per vertex).
coords = [0.0] * len(collection) * 3

### Fast access.
collection.foreach_get("co", coords)

### Python equivalent (per-element iteration is much slower).
for i, vert in enumerate(collection):
    coords[i * 3], coords[i * 3 + 1], coords[i * 3 + 2] = vert.co
```
foreach_set ( attr , seq )

Quick writes of a basic-type attribute stored across a collection.

Parameters :

- attr ( str ) – Name of the item attribute to write (for example co or
select ). The attribute must be a basic type (bool, int or float).

For geometry attribute types, see Attribute.data_type.

- seq ( Sequence [ bool | int | float ] | buffer ) – Sequence or buffer containing flattened values.
For array attributes, the length must be len(collection) * array_length .

Only works for 'basic type' properties (bool, int and float)!
seq must be uni-dimensional, multi-dimensional arrays (like array of vectors) will be re-created from it.

```python
import bpy

mesh = bpy.context.object.data
collection = mesh.vertices

### Flatten all Z coordinates to zero (X, Y, Z per vertex).
coords = [0.0] * len(collection) * 3
collection.foreach_get("co", coords)
for i in range(2, len(coords), 3):
    coords[i] = 0.0

### Fast assignment.
collection.foreach_set("co", coords)

### Python equivalent (per-element iteration is much slower).
for i, vert in enumerate(collection):
    vert.co = (coords[i * 3], coords[i * 3 + 1], coords[i * 3 + 2])
```

[Related references](INDEX.md).
