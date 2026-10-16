# mathutils.Vector: overview

class mathutils. Vector ( seq = (0.0, 0.0, 0.0) , / ) 

A handle onto Blender's Vector objects.

Parameters :

seq ( Sequence [ float ] ) – The vector's entries, given as a sequence holding two or more.

```python
import mathutils

# Unit vector along the Z axis.
vec = mathutils.Vector((0.0, 0.0, 1.0))

### Unit length vector.
vec_a = vec.normalized()

vec_b = mathutils.Vector((0.0, 1.0, 2.0))

vec2d = mathutils.Vector((1.0, 2.0))
vec3d = mathutils.Vector((1.0, 0.0, 0.0))
vec4d = vec_a.to_4d()

### Other `mathutils` types.
quat = mathutils.Quaternion()
matrix = mathutils.Matrix()

### Comparison operators can be done on Vector classes:

### (In)equality operators == and != test component values, e.g. 1,2,3 != 3,2,1
vec_a == vec_b
vec_a != vec_b

### Ordering operators >, >=, > and vec_b
vec_a >= vec_b
vec_a
```

[Related references](INDEX.md).
