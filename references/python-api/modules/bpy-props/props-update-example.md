# bpy.props: Update Example

```python
import bpy

### Assign a collection.
class SceneSettingItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Test Property", default="Unknown")
    value: bpy.props.IntProperty(name="Test Property", default=22)

bpy.utils.register_class(SceneSettingItem)

bpy.types.Scene.my_settings = bpy.props.CollectionProperty(type=SceneSettingItem)

### Assume an armature object selected.
print("Adding 2 values!")

my_item = bpy.context.scene.my_settings.add()
my_item.name = "Spam"
my_item.value = 1000

my_item = bpy.context.scene.my_settings.add()
my_item.name = "Eggs"
my_item.value = 30

for my_item in bpy.context.scene.my_settings:
    print(my_item.name, my_item.value)
```

### Update Example 

It can be advantageous to do an operation when a quality is moved and may be
utilized to refresh other qualities or link with external information.

Every qualities specify upgrade operations excluding for CollectionProperty.

Warning

Keep in mind that these functions may be carried out in concurrent framework.

Warning

If the quality is part of an Operator, the upgrade operation's opening
factor will be an OperatorProperties case, rather than an case
of the tool itself. This implies you cannot obtain additional inner functions
of the tool, merely its additional qualities.

```python
import bpy

def update_func(self, context):
    print("my test function", self)

bpy.types.Scene.testprop = bpy.props.FloatProperty(update=update_func)

bpy.context.scene.testprop = 11.0

### >>> my test function
```

[Related references](INDEX.md).
