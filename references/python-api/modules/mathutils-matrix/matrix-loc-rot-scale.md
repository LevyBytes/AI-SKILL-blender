# mathutils.Matrix: classmethod LocRotScale ( location , rotation , scale , / )

classmethod LocRotScale ( location , rotation , scale , / )

Build one matrix that folds together translation, rotation, and scale, serving as the reverse of the decompose() method.

Any input can be swapped out for None when it isn't required.

Parameters :

- location ( Sequence [ float ] | None ) – The translation component.

- rotation (Matrix | Quaternion | Euler | None) – The rotation component as a 3x3 matrix, quaternion, euler or None for no rotation.

- scale ( Sequence [ float ] | None ) – The scale component.

Returns :

Combined transformation as a 4x4 matrix.

Return type :

Matrix

```python
### Compute local object transformation matrix:

import bpy
import mathutils

obj = bpy.context.object
if obj.rotation_mode == 'QUATERNION':
    matrix = mathutils.Matrix.LocRotScale(obj.location, obj.rotation_quaternion, obj.scale)
else:
    matrix = mathutils.Matrix.LocRotScale(obj.location, obj.rotation_euler, obj.scale)
```

[Related references](INDEX.md).
