# bpy.types.PreferencesInput: ndof_navigation_mode

ndof_navigation_mode

3D Mouse Navigation Mode (default 'OBJECT' )

- OBJECT
Object – Feels like reaching into the screen to grip the model directly. Nudge the 3D Mouse cap leftward and the model slides left; nudge it right and it slides right.

- FLY
Fly – Treats the 3D Mouse like a camera. Press into the scene to drive the camera deeper in, as though piloting through it. Pan & zoom are also inverted for 2D views.

- DRONE
Drone – Behaves like Fly Mode, except tilting the cap forward while looking down leaves the camera's altitude untouched..

Type :

Literal[‘OBJECT’, ‘FLY’, ‘DRONE’]

[Related references](INDEX.md).
