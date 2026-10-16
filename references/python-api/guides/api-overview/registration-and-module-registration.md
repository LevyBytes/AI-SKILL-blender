# API Overview: Registration, Module Registration

```python
import bpy
class AwesomeRaytracer(bpy.types.RenderEngine):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.my_var = 42
      ...
```

Warning

Before any data on the object is touched, you have to invoke the Blender-defined parent constructor —
that applies to access from the __init__() functions of any other parent types too.

Warning

Since Blender 4.4, invoking the parent's __init__() function is mandatory. Go with the 'generic' signature, given that the only caller of these functions is usually Blender's own internal BPY code. Whatever arguments reach the constructor are wholly internal data and can change with the implementation.

Sadly, the error you get when the expected constructor goes uncalled can be rather cryptic and unhelpful. As a rule it complains that some (python) object couldn't be built:

MemoryError: couldn't create bpy_struct object

For Operators the wording runs more like:

RuntimeError: could not create instance of <`OPERATOR_OT`_identifier> to call callback function execute

Note

With complex or multiple inheritance in play, super() can come up short — the Blender-defined parent may not sit first in the MRO. The safer approach is then to invoke that Blender-defined parent's constructor by name, ahead of every other. As an illustration:

```python
import bpy
class FancyRaytracer(AwesomeRaytracer, bpy.types.RenderEngine):
   def __init__(self, *args, **kwargs):
      bpy.types.RenderEngine.__init__(self, *args, **kwargs)
      AwesomeRaytracer.__init__(self, *args, **kwargs)
      self.my_var = 42
      ...
```

Note

Writing a custom __new__() function is something we strongly advise against — it's untested and, for now, not treated as supported. Going ahead with it brings a genuine risk of crashes or of corrupting Blender's internal data. If you do write one regardless, it must accept the same pair of generic arguments (positional and keyword) and forward them to the parent's __new__() whenever it actually constructs a new object.

Note

Because of how CPython is implemented internally, Blender types defined in C++ presently neither declare nor make use of a __del__() destructor (otherwise known as tp_finalize() ). Since that function isn't there unless you write it yourself, a super().__del__() call from inside a subclass's __del__() trips this error: AttributeError: 'super' object has no attribute '__del__' . Should you genuinely need the MRO 'parent' destructor, your calling code has to confirm it exists beforehand — for example along these lines:
getattr(super(), "__del__", lambda self: None)(self)

### Registration

### Module Registration

A startup-loaded Blender module is required to provide both a register() and an unregister() function. Those two are the sole entry points Blender calls into your code; everything else is just a plain Python module.

Here's roughly what a minimal Blender Python module might look like:

```python
import bpy

class SimpleOperator(bpy.types.Operator):
    """ See example above """

def register():
    bpy.utils.register_class(SimpleOperator)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)

if __name__ == "__main__":
    register()
```

You'll usually see these at the foot of the script that registers the classes, sometimes adding menu items too. They're also usable for internal needs, like setting up data for your own tools — just bear in mind register won't run again when a fresh blend-file loads.

A register/unregister pair is precisely what lets add-ons be switched on and off, and scripts be reloaded, without a Blender restart. Were those register calls placed directly in the script body, they'd run at import time, blurring the line between importing a module and loading its classes into Blender. That gets messy as soon as one script pulls classes in from another module, since it becomes hard to keep track of what loads and when.

Those final two lines serve testing only:

[Related references](INDEX.md).
