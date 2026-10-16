# bpy.types.PropertyGroup: overview

class bpy.types. PropertyGroup ( bpy_struct ) 

Group of ID properties
## PropertyGroup(bpy_struct)

### PropertyGroup(bpy_struct)
### Custom Properties 

A PropertyGroup serves as the foundation class for property sets that are defined on the fly.

You can use them to attach your own custom types onto existing Blender data, and
those types stay animatable, reachable from the user interface, and reachable from Python.

Note

While the values placed on Blender data persist to disk, the class
definitions do not — so each time Blender starts the class must be
registered once more.

The recommended approach is an add-on that runs at startup and registers
your properties there.

Note

A PropertyGroup has to be registered before it can be attached to Blender data.

See also

The property types used inside class declarations all live in bpy.props

```python
import bpy

class MyPropertyGroup(bpy.types.PropertyGroup):
    custom_1: bpy.props.FloatProperty(name="My Float")
    custom_2: bpy.props.IntProperty(name="My Int")

bpy.utils.register_class(MyPropertyGroup)

bpy.types.Object.my_prop_grp = bpy.props.PointerProperty(type=MyPropertyGroup)

### Test this worked.
bpy.data.objects[0].my_prop_grp.custom_1 = 22.0
```

base class — bpy_struct

subclasses —
OperatorFileListElement, OperatorMousePath, OperatorStrokeElement, SelectedUvElement

[Related references](INDEX.md).
