# bpy.types.bpy_struct: keyframe_insert ( data_path , * , index = -1 , frame = bpy.context.scene.frame_current , group = '' , options = set() , keytype = 'KEYFRAME' )

keyframe_insert ( data_path , * , index = -1 , frame = bpy.context.scene.frame_current , group = '' , options = set() , keytype = 'KEYFRAME' )

Drops a keyframe on the given property, creating fcurves and animation data as required.

Parameters :

- data_path ( str ) – path to the property to key, analogous to the fcurve's data path.

- index ( int ) – array index of the property to key.
Defaults to -1 which will key all indices or a single channel if the property is not an array.

- frame ( float ) – The frame on which the keyframe is inserted, defaulting to the current frame.

- group ( str ) – The name of the group the F-Curve should be added to if it doesn't exist yet.

- options ( set [ Literal [ '`INSERTKEY_NEEDED`' , '`INSERTKEY_VISUAL`' , '`INSERTKEY_REPLACE`' , '`INSERTKEY_AVAILABLE`' , '`INSERTKEY_CYCLE_AWARE`' ] ] ) – Optional set of flags:

- `INSERTKEY_NEEDED` Only insert keyframes where they're needed in the relevant F-Curves.

- `INSERTKEY_VISUAL` Insert keyframes based on 'visual transforms'.

- `INSERTKEY_REPLACE` Only replace already existing keyframes.

- `INSERTKEY_AVAILABLE` Only insert into already existing F-Curves.

- `INSERTKEY_CYCLE_AWARE` Take cyclic extrapolation into account (Cycle-Aware Keying option).

- keytype ( Literal [ 'KEYFRAME' , 'BREAKDOWN' , '`MOVING_HOLD`' , 'EXTREME' , 'JITTER' , 'GENERATED' ] ) – Type of the key.

Returns :

Success of keyframe insertion.

Return type :

bool

Here is the most basic way to insert a keyframe from Python.

```python
import bpy

obj = bpy.context.object

### Set the keyframe at frame 1.
obj.location = (3.0, 4.0, 10.0)
obj.keyframe_insert(data_path="location", frame=1)
```

Bear in mind that keying data paths with nested properties has to be
performed on the ID subclass — here the Armature rather
than the bone.

```python
import bpy
from bpy.props import (
    FloatProperty,
    PointerProperty,
)

### Define a nested property.
class MyPropGroup(bpy.types.PropertyGroup):
    nested: FloatProperty(name="Nested", default=0.0)

### Register it so its available for all bones.
bpy.utils.register_class(MyPropGroup)
bpy.types.Bone.my_prop = PointerProperty(
    type=MyPropGroup,
    name="MyProp",
)

### Get a bone.
obj = bpy.data.objects["Armature"]
arm = obj.data

### Set the keyframe at frame 1.
arm.bones["Bone"].my_prop.nested = 10
arm.keyframe_insert(
    data_path='bones["Bone"].my_prop.nested',
    frame=1,
    group="Nested Group",
)
```

[Related references](INDEX.md).
