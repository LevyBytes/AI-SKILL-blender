# Render Baking: Setup, Settings

## Render Baking

### Render Baking 

Cycles lets you bake shaders and lighting down into image textures.
The usual reasons make a short list:

- Writing out base color, normal maps and similar textures so a game engine can take them.

- Laying down ambient occlusion or procedural textures to seed texture painting or later edits.

- Building light maps that supply global illumination, or that make a game render quicker.

### Setup 

Baking asks that the mesh own a UV map together with either a Color Attribute or an Image Texture node holding an image to receive the bake.
Whichever of the two is active, the Image Texture node or the Color Attribute, serves as the bake target.

Pull out Render Bake for demanding light and shadow work, AO say, or the soft shadows of area lights. Bake AO once for your main objects and you skip it on the full render, shaving render time.
Cycles bakes with the render settings (samples, bounces, …) in play.
So baked textures should land matching what the rendered scene gives back.

### Settings 

Reference

Panel :

Render ‣ Bake

Bake
Fires off the bake using whatever settings stand right now.

Bake from Multires
Bakes a Normal or Displacement map right off a mesh wearing a Multiresolution Modifier.

It sets two of the modifier's resolution levels side by side:

- Viewport Levels The coarse base mesh stands in here.

- Render Levels The fine, detailed mesh stands in here.

What the bake writes out is the gap between those levels, so finely sculpted detail ends up captured in a texture map.

Bake Type
Picks which surface information gets drawn out of the Multiresolution modifier.
See Bake Types for more information.

Normals :

Records how the surface normal direction differs between the two levels.

Displacement :

Records height differences as a grayscale displacement map.

Vector Displacement :

Records each point's full 3D offset, writing it out as a vector displacement map.

[Related references](INDEX.md).
