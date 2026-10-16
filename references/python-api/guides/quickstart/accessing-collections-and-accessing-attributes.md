# Quickstart: Accessing Collections, Accessing Attributes, Data Creation/Removal

```pycon
>>> bpy.data.materials
```

#### Accessing Collections

You'll see that collection members can be reached either by index or by string. That's unlike Python dictionaries, where only one applies; here both work, though keep in mind a member's index can shift while Blender is running.

```pycon
>>> list(bpy.data.objects)
[bpy.data.objects["Cube"], bpy.data.objects["Plane"]]
```

```pycon
>>> bpy.data.objects['Cube']
bpy.data.objects["Cube"]
```

```pycon
>>> bpy.data.objects[0]
bpy.data.objects["Cube"]
```

#### Accessing Attributes

After you've got hold of a data-block (a material, object, collection, and the like), reading or setting its attributes feels much like flipping a setting in the graphical interface. Indeed, each button's tooltip spells out the Python attribute, which is handy for tracking down which setting a script should touch.

```pycon
>>> bpy.data.objects[0].name
'Camera'
```

```pycon
>>> bpy.data.scenes["Scene"]
bpy.data.scenes['Scene']
```

```pycon
>>> bpy.data.materials.new("MyMaterial")
bpy.data.materials['MyMaterial']
```

When you're figuring out which data to reach for, the Python Console (a space type of its own) comes in handy. With auto-complete on tap, it's a quick route to browsing the data in your file.

A sample data path that the console makes easy to discover:

```pycon
>>> bpy.data.scenes[0].render.resolution_percentage
100
>>> bpy.data.scenes[0].objects["Torus"].data.vertices[0].co.x
1.0
```

#### Data Creation/Removal

Coming from other Python APIs, it might catch you off guard that you can't spin up fresh data-blocks in the bpy API by calling the class itself:

[Related references](INDEX.md).
