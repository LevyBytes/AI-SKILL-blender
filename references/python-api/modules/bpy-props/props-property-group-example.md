# bpy.props: PropertyGroup Example

The complete program is in the [upstream source](https://docs.blender.org/api/5.1/bpy.props.html#operator-example).

### PropertyGroup Example 

PropertyGroups can be utilized for gathering tailored adjustments into sole worth
to prevent numerous distinctive adjustments combined altogether.

```python
import bpy

class MaterialSettings(bpy.types.PropertyGroup):
    my_int: bpy.props.IntProperty()
    my_float: bpy.props.FloatProperty()
    my_string: bpy.props.StringProperty()

bpy.utils.register_class(MaterialSettings)

bpy.types.Material.my_settings = bpy.props.PointerProperty(type=MaterialSettings)

### Test the new settings work.
material = bpy.data.materials[0]

material.my_settings.my_int = 5
material.my_settings.my_float = 3.0
material.my_settings.my_string = "Foo"
```

### Collection Example 

Tailored qualities can be supplied to every subclass of an ID ,
Bone and PoseBone .

[Related references](INDEX.md).
