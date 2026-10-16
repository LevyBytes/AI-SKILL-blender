# Troubleshooting Errors & Crashes: Help! My script crashes Blender

## Troubleshooting Errors & Crashes

### Troubleshooting Errors & Crashes

### Help! My script crashes Blender

TL;DR Don't hang on to direct references to Blender data (of whatever kind) while you're editing the container holding that data, or anywhere undo/redo might fire (for instance during a modal operator's run). Instead, work through indices — or other things Python stores by value, such as string keys — that let you fetch the data you're after.

In an ideal world Python could never crash Blender, but in practice there are spots in the API where a crash is reachable. Technically that's an API bug, yet patching it would require memory checks on every single access: most crashes trace back to Python objects pointing straight at Blender's memory, and once that memory is freed or moved, any further Python access to it can take the script down. Fixing it properly would either make scripts crawl, or demand a wholly different API that never references the memory directly.

Some broad pointers for steering clear of these traps:

- Watch your memory footprint,
above all with large lists, since Blender can crash purely by exhausting memory.

- A lot of stubborn crashes boil down to referencing freed data; when you delete data make sure you're not still holding a reference to it.

- Re-allocation lands you in the same trouble
(e.g. piling many items into a Collection can force the backing container's memory to move, which voids every reference you held to existing items).

- Long-lived modules or classes that persist as Blender runs
shouldn't hold onto data the user could remove; rather,
have the script re-read whatever it needs from the context on each activation.

- Crashes can be intermittent — surfacing more readily on certain setups or operating systems.

- Tread carefully with recursion, which is remarkably good at masking the problems described here.

- See the closing Unfortunate Corner Cases section for some known exceptions that break.

Note

To pin down which line of your script crashes, the faulthandler module helps.
See the Faulthandler docs.

The crash itself may sit inside Blender's C/C++ code, but this can go a long way toward locating the part of the script that triggers it.

Note

A few container edits are in fact safe, because they never relocate existing data
(e.g. linked-list containers never move existing items when others are added or removed).

But telling the safe cases from the unsafe ones demands a deep grasp of Blender's internals. So unless you're prepared to wade into the RNA C implementation, the simpler stance is to always assume that modifying a container — in any way at all — invalidates references into it.

Do not:

```python
class TestItems(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()

bpy.utils.register_class(TestItems)
bpy.types.Scene.test_items = bpy.props.CollectionProperty(type=TestItems)

first_item = bpy.context.scene.test_items.add()
for i in range(100):
    bpy.context.scene.test_items.add()

### This is likely to crash, as internal code may re-allocate
### the whole container (the collection) memory at some point.
first_item.name = "foobar"
```

Do:

```python
class TestItems(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()

bpy.utils.register_class(TestItems)
bpy.types.Scene.test_items = bpy.props.CollectionProperty(type=TestItems)

first_item = bpy.context.scene.test_items.add()
for i in range(100):
    bpy.context.scene.test_items.add()

### This is safe, we are getting again desired data *after*
### all modifications to its container are done.
first_item = bpy.context.scene.test_items[0]
first_item.name = "foobar"
```

[Related references](INDEX.md).
