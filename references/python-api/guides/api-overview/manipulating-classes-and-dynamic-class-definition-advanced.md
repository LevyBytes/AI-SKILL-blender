# API Overview: Manipulating Classes, Dynamic Class Definition (Advanced)

```python
### Create new property group with a sub property:
### bpy.data.materials[0].my_custom_props.sub_group.my_float
import bpy

class MyMaterialSubProps(bpy.types.PropertyGroup):
    my_float: bpy.props.FloatProperty()

class MyMaterialGroupProps(bpy.types.PropertyGroup):
    sub_group: bpy.props.PointerProperty(type=MyMaterialSubProps)

def register():
    bpy.utils.register_class(MyMaterialSubProps)
    bpy.utils.register_class(MyMaterialGroupProps)
    bpy.types.Material.my_custom_props = bpy.props.PointerProperty(type=MyMaterialGroupProps)

def unregister():
    del bpy.types.Material.my_custom_props
    bpy.utils.unregister_class(MyMaterialGroupProps)
    bpy.utils.unregister_class(MyMaterialSubProps)

if __name__ == "__main__":
    register()
```

Important

Register the innermost class ahead of the rest, and make sure unregister() mirrors register() in reverse.

#### Manipulating Classes

Properties can be tacked on and stripped off while Blender runs — normally during register or unregister, though for some special situations it can be handy to reshape types as the script executes.

For example:

```python
### Add a new property to an existing type.
bpy.types.Object.my_float: bpy.props.FloatProperty()
### Remove it.
del bpy.types.Object.my_float
```

PropertyGroup subclasses of your own respond to the same technique just as well.

```python
class MyPropGroup(bpy.types.PropertyGroup):
    pass
MyPropGroup.my_float: bpy.props.FloatProperty()
```

Which amounts to the same thing as:

```python
class MyPropGroup(bpy.types.PropertyGroup):
    my_float: bpy.props.FloatProperty()
```

#### Dynamic Class Definition (Advanced)

At times what specifies some data sits outside Blender — the shader definitions of an external render engine, for example — and it can be worthwhile to register them as types and drop them again dynamically.

[Related references](INDEX.md).
