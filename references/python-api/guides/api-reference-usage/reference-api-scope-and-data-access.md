# API Reference Usage: Reference API Scope, Data Access, ID Data, Simple Data Access, Nested Properties

## API Reference Usage

### API Reference Usage

The web of interconnected data types in Blender ships with an auto-generated reference API. That reference usually holds whatever a script author needs, yet newcomers tend to find it awkward to navigate. The aim of this page is to make the reference API approachable.

### Reference API Scope

What the reference API documents is bpy.types — the types you reach either through bpy.context (the user's current context) or through bpy.data (the data inside the blend-file).

It does not extend to modules like bmesh and aud, since those sit outside Blender's data API; nothing on this page carries over to them.

### Data Access

By far the usual reason to open the reference API is to work out the route to some piece of data in the blend-file. It pays to first understand ID data-blocks, because a great many properties are described in relation to them.

### ID Data

At the top level, data in Blender is held inside ID data-blocks. The interface keeps this mostly invisible, yet once you move to development it's something you have to know about. Texture, Image, Armature, World, Workspace, Mesh, Object, Collection and Scene are all examples of ID data types; for the exhaustive set, look at what subclasses bpy.types.ID.

Traits common to ID data-blocks:

- Because IDs belong to the blend-file, opening a different blend-file swaps in a whole fresh set of them.

- From Python they are reached through bpy.data.* .

- Every data-block carries a unique .name attribute that the interface shows.

- An ID stores its animation under .animation_data .

- Only IDs may be linked across blend-files.

- Python can create, duplicate and delete IDs.

- A dedicated garbage-collection mechanism drops IDs that go unused when you save.

- Where one data-block points at some outside data, that referenced thing is generally an ID data-block too.

### Simple Data Access

Here a short Python script nudges an object's position. The starting task is to track down where that data actually lives.

Locate the control in the interface at Properties editor -> Object -> Transform -> Location . Opening the button's context menu and choosing Online Python Reference jumps you to:
bpy.types.Object.location.
Such reference pages frequently say little beyond what the tooltip already told you, though a number of them carry examples (usually near the top). The payoff is knowing you reach it through .location and that it holds three floats in an array.

What remains is finding the entry point for objects: scroll to the references section at the foot of the page. Objects show up in plenty of references, but among the most frequent ways in is through the context. It's tempting to feel swamped here, given how widely Object is referenced — across modifiers, functions, textures and constraints. Still, when your goal is whatever the user has currently selected, the bpy.context references are normally all you need to consult.

Even there the list runs fairly long, and skimming it reveals that most entries are tied to a particular mode. Suppose your tool only operates in Weight Paint Mode — then weight_paint_object is the right pick. To instead grab whatever the user selected last, hunt for the active members. Reaching a single active member that follows the user's selection is a standard Blender pattern: see active_bone , active_pose_bone , active_node , etc., and for this scenario active_object fits.

That gives you everything required to reach the active object's location.

```python
bpy.context.active_object.location
```

Enter that in the Python console to see what comes back. Objects also commonly appear in the reference under bpy.types.BlendData.objects.

Note

You won't see it written as bpy.data.objects in the docs;
the reason is that bpy.data is one instance of bpy.types.BlendData ,
so that class is where the documentation directs you.

Since bpy.data.objects holds a collection, you have to index into one of its members:

```python
bpy.data.objects["Cube"].location
```

### Nested Properties

That first example stayed simple, because location belongs to Object and the context hands it to you directly.

A few trickier cases follow:

[Related references](INDEX.md).
