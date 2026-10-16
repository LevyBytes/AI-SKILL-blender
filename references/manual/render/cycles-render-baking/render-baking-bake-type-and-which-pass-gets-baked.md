# Render Baking: Bake Type, Which pass gets baked.

Bake Type
Which pass gets baked.

Combined :

Rolls in every material, texture and light bar specularity.
The passes feeding the combined pass can each be flipped on or off to shape the final map.

Ambient Occlusion :

Records ambient occlusion per the World panels, ignoring every scene light.

Shadow :

Captures the lighting along with the shadows it throws.

Position :

Writes world-space position into the RGB channels.
Each pixel carries the surface point's XYZ position, taken relative to the scene origin.

Normal :

Lays the normals down onto an RGB image.

UV :

The mapped UV coordinates, flagging where on a mesh a texture sits.
They ride the image's red and green channels; the blue channel holds a flat 1 and carries no data.

Roughness :

Writes out a material's roughness as its own pass.

Emit :

Writes out a material's Emission, its Glow color.

Environment :

Writes out the environment, namely the scene's world surface shader, onto whatever objects you chose, as rays fired from the world origin would see it.

Diffuse :

Writes out a material's diffuse component as its own pass.

Glossy :

Writes out a material's glossiness as its own pass.

Transmission :

Writes out a material's transmission as its own pass.

View From
Where the reflection rays set out.

Above Surface :

Cast the rays from over the surface.

Active Camera :

Cast the rays from where the active camera sits.

[Related references](INDEX.md).
