# Dynamic operator registration

```python
import bpy

for i in range(10):
    idname = "object.operator_{:d}".format(i)

    def func(self, context):
        print("Hello World", self.bl_idname)
        return {'FINISHED'}

    op_class = type(
        "DynOp{:d}".format(i),
        (bpy.types.Operator, ),
        {"bl_idname": idname, "bl_label": "Test", "execute": func},
    )
    bpy.utils.register_class(op_class)
```

Note

Here the class is defined by calling type() .
In Python that's an alternative way to write a class, and it lends itself better to building classes on the fly.

Invoking the operators built just above:

```pycon
>>> bpy.ops.object.operator_1()
Hello World OBJECT_OT_operator_1
{'FINISHED'}
```

```pycon
>>> bpy.ops.object.operator_2()
Hello World OBJECT_OT_operator_2
{'FINISHED'}
```

[Related references](INDEX.md).
