# bpy.types.View3DShading: background_color, background_type

background_color

The RGB triple applied when a custom viewport background is chosen (array of 3 items, in [0, 1], default (0.05, 0.05, 0.05))

Type :

mathutils.Color
background_type

Chooses what fills the viewport background (default 'THEME' )

- THEME
Theme – Take the background tint straight from the active theme.

- WORLD
World – Derive the background from the scene's world.

- VIEWPORT
Custom – Apply a fixed color that affects only this viewport.

Type :

Literal['THEME', 'WORLD', 'VIEWPORT']

[Related references](INDEX.md).
