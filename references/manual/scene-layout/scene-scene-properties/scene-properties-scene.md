# Scene Properties: Scene

## Scene Properties

### Scene Properties

### Scene

Reference

Panel :

Properties ‣ Scene ‣ Scene

Camera
Designates the rendering perspective.
You can also set the rendering perspective in the 3D Viewport using Ctrl - Numpad0 .

Background Scene
Provides the ability to display a scene as a backdrop,
useful when focusing on foreground animation, for instance,
without background elements obstructing the workspace.

This scene can include its own movement timeline, physics effects, etc,
though you must activate it via the Scene data-block menu to adjust its internals.

Background Scenes can themselves reference another Background Scene (they're embedded recursively).
This allows expanding current scenes by setting them as a backdrop
to a newly built scene where modifications happen.

Tip

This pairs effectively with Linking to a Scene,
where one blend-file supplies the context, reusable in multiple locations.

Active Clip
Assigns a Movie Clip usable in
Motion Tracking Constraints or a camera's Background Images.

[Related references](INDEX.md).
