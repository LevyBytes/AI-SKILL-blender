# API Overview: Class Registration, Inter-Class Dependencies

```python
if __name__ == "__main__":
    register()
```

It allows the script to run directly in the text editor for testing your edits. Import the script as a module and that register() call stays quiet, because __main__ is reserved for running a file directly.

### Class Registration

When you register a class, its definition gets loaded into Blender and joins the functionality already there. Once loaded, it's reachable from bpy.types, where you address it by bl_idname rather than by the name the class originally had.

Note

A few class names can't be promised to be unique, and those are the exceptions here.
For them, reach for: bpy.types.Struct.bl_rna_get_subclass_py().

As it loads a class, Blender runs sanity checks confirming that every required property and function is present, that properties carry the right type, and that functions take the correct number of arguments.

Mostly this won't concern you, but if the class definition has a problem it'll surface at registration:

Give the function the arguments def execute(self, context, spam) and you'll trip an exception:

ValueError: expected Operator, SimpleOperator class "execute" function to have 2 args, found 3

Setting bl_idname = 1 throws:

TypeError: validating class error: Operator.bl_idname expected a string type, not int

#### Inter-Class Dependencies

As you customize Blender you may want to gather your own settings in one place; after all they'll have to live next to other scripts. Grouping them means defining classes, and for groups nested in groups, or collections inside groups, there's no dodging the question of registration/unregistration order.

Custom property groups are themselves classes that need registering.

Say, for example, you want a custom engine's material settings stored:

```python
### Create new property:
### bpy.data.materials[0].my_custom_props.my_float
import bpy

class MyMaterialProps(bpy.types.PropertyGroup):
    my_float: bpy.props.FloatProperty()

def register():
    bpy.utils.register_class(MyMaterialProps)
    bpy.types.Material.my_custom_props = bpy.props.PointerProperty(type=MyMaterialProps)

def unregister():
    del bpy.types.Material.my_custom_props
    bpy.utils.unregister_class(MyMaterialProps)

if __name__ == "__main__":
    register()
```

Note

Registration of the class has to happen before any property uses it; skip that and you'll get an error:

ValueError: bpy_struct "Material" registration error: my_custom_props could not register

[Related references](INDEX.md).
