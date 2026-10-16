# bpy.msgbus: properties

### Limitations

The message bus fires on RNA-layer modifications. Changes that trigger notifications:

- Python API updates, e.g. some_object.location.x += 3 .

- Interactive edits via UI sliders, input fields, and buttons.

These do not generate message bus alerts:

- Viewport manipulation of objects.

- Animation playback-driven updates.

Side effects of msgbus callbacks skip undo integration, so users may erase them with Undo then Redo.

Unlike direct property callbacks, message bus events queue until all active operators conclude. Each property fires its callback a maximum of once per update pass, even if modified multiple times.

### Example Use

Below demonstrates subscription to transformations on the focused object.

```python
import bpy

# Any Python object can act as the subscription's owner.
owner = object()

subscribe_to = bpy.context.object.location


def msgbus_callback(*args):
    # This will print:
    # Something changed! (1, 2, 3)
    print("Something changed!", args)


bpy.msgbus.subscribe_rna(
    key=subscribe_to,
    owner=owner,
    args=(1, 2, 3),
    notify=msgbus_callback,
)
```

Certain properties become Python-wrapped on retrieval. To establish subscriptions, unwrap them with datablock.path_resolve(\"property_name\", False) :

```python
import bpy

subscribe_to = bpy.context.object.path_resolve("name", False)
```

Subscriptions can also target properties across all instances of a given type:

```python
import bpy

subscribe_to = (bpy.types.Object, "location")
```

[Related references](INDEX.md).
