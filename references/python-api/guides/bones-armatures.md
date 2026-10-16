# Bones & Armatures

## Bones & Armatures

### Bones & Armatures

### Edit Bones, Pose Bones, Bone… Bones

In Blender, armature bones are held in three separate data structures. If you reach a bone through the wrong one of them, the properties you actually need may be out of reach.

Note

Throughout the examples below, bpy.context.object is taken to be an armature object.

### Edit Bones

Edit bones live in bpy.context.object.data.edit_bones ; to touch them the armature must first be in Edit-Mode (they simply don't exist in Object or Pose-Mode). Reach for these when you want to spawn new bones, set head/tail or roll, rewire parenting between bones, and so on.

An example with bpy.types.EditBone , which only runs on an armature in Edit-Mode:

```pycon
>>> bpy.context.object.data.edit_bones["Bone"].head = Vector((1.0, 2.0, 3.0))
```

Outside Edit-Mode this comes back empty:

```pycon
>>> mybones = bpy.context.selected_editable_bones
```

Only while in Edit-Mode does this yield an edit bone:

```pycon
>>> bpy.context.active_bone
```

### Bones (Object-Mode)

Plain bones sit in bpy.context.object.data.bones . They exist in Object-Mode and expose several properties you can edit, with the caveat that head and tail are read-only.

An example with bpy.types.Bone , run from Object or Pose-Mode; outside Edit-Mode it returns a bone, not an edit bone:

```pycon
>>> bpy.context.active_bone
```

This works because the setting — as it is in Blender — can be changed from whichever mode you're in:

```pycon
>>> bpy.context.object.data.bones["Bone"].use_deform = True
```

Readable, but you can't write to it:

```pycon
>>> tail = myobj.data.bones["Bone"].tail
```

### Pose Bones

Pose bones are found in bpy.context.object.pose.bones . This is the home of animation data — the animatable transforms land on pose bones, and so do constraints and IK settings.

Some bpy.types.PoseBone examples, usable from Object or Pose-Mode:
```python
### Gets the name of the first constraint (if it exists).
bpy.context.object.pose.bones["Bone"].constraints[0].name

### Gets the last selected pose bone (Pose-Mode only).
bpy.context.active_pose_bone
```

Note

Observe that the pose hangs off the object instead of the object data; that's exactly what lets two or more objects share one armature while striking different poses.

Note

In a strict sense pose bones aren't bones at all; they capture the armature's present state, which lives on the object (bpy.types.Object) and not on the armature data (bpy.types.Armature). From any pose bone the actual bone remains reachable through bpy.types.PoseBone.bone.

### Armature Mode Switching

Scripts that handle armatures often have to hop between modes, and when you leave Edit-Mode you must be careful not to keep holding edit bones or their head/tail vectors. Reaching for them afterward will crash Blender, so it's vital the script keeps the code for different modes cleanly partitioned.

This bites mainly with Edit-Mode, because pose data can be edited without ever entering Pose-Mode — though to drive operators you may still have to switch into Pose-Mode.

[Related references](INDEX.md).
