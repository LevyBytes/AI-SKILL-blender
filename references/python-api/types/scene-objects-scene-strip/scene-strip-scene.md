# bpy.types.SceneStrip: scene, scene_camera, scene_input

scene

Scene that this strip uses

Type :

Scene
scene_camera

Use a camera other than the scene's active one

Type :

Object
scene_input

Which input the Scene strip draws from (default 'CAMERA' )

- CAMERA
Camera – Take the Scene's 3D camera as the input.

- SEQUENCER
Sequencer – Take the Scene's Sequencer timeline as the input.

Type :

Literal[‘CAMERA’, ‘SEQUENCER’]

[Related references](INDEX.md).
