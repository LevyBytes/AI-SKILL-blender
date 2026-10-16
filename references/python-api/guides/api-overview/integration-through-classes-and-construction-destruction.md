# API Overview: Integration through Classes, Construction & Destruction

### Integration through Classes

Running scripts in the text editor is great for trying things out, but you'll want to extend Blender so your tools sit alongside the rest of its built-in functionality.

The Blender Python API permits integration for:

- bpy.types.Panel

- bpy.types.Menu

- bpy.types.Operator

- bpy.types.PropertyGroup

- bpy.types.KeyingSet

- bpy.types.RenderEngine

The shortness of that list is on purpose. More involved capabilities — shader nodes, new object types, mesh modifiers and the like — remain, for now, the province of C/C++.

To integrate with Python, Blender provides methods common across all types. It works by subclassing a Blender class in Python; that subclass then inherits the variables and functions its parent defines, all set up in advance to talk to Blender.

For example:

```python
import bpy
class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Tool Name"

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}

bpy.utils.register_class(SimpleOperator)
```

Notice first that the subclass it defines belongs to bpy.types — the norm for every class that integrates with Blender, and what lets registration distinguish an Operator from a Panel. The two class properties each begin with bl_ , a convention separating Blender's properties from ones of your own. After that is the execute function, which receives the operator instance plus the running context; no common prefix applies to functions. Last, register is called to take the class and load it into Blender. See Class Registration.

As for inheritance, Blender imposes no restriction on what styles of class inheritance you employ; when registering, the checks will consult whatever functions and attributes the parent classes define.

Class mix-in example:

```python
import bpy
class BaseOperator:
    def execute(self, context):
        print("Hello World BaseClass")
        return {'FINISHED'}

class SimpleOperator(bpy.types.Operator, BaseOperator):
    bl_idname = "object.simple_operator"
    bl_label = "Tool Name"

bpy.utils.register_class(SimpleOperator)
```

Note

An exception is modal operators, which hold their instance variable for as long as Blender runs; see the modal operator template.

So after a class has been registered, it falls to Blender to instantiate it and invoke its functions. Indeed you can't create instances of these classes from your script as most Python APIs would let you. Running an operator means going through the operator API instead, e.g:

```python
import bpy
bpy.ops.object.simple_operator()
```

User interface classes are handed a context to draw in — buttons, window, file header, toolbar, and so on — and they're drawn whenever that area shows, so Python scripts never call them directly.

### Construction & Destruction

Notice that in the examples above the classes never define an __init__(self) function. As a rule you shouldn't need custom constructors or destructors, and they're not recommended.

A class instance's lifetime is typically very brief (see also the dedicated section); a panel, for one, gets a brand-new instance on every redraw. A few other types, such as bpy.types.Operator, are handled in an even more intricate way internally, which can spawn several instantiations for a single operator run.

There are a handful of cases where an __init__() does earn its keep, e.g. when subclassing a bpy.types.RenderEngine. When you do, the parent's matching function must always be called, or Blender's internal initialization won't run properly:

[Related references](INDEX.md).
