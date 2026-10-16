# Object: Motion Blur, Shading, Shadow Terminator, Fast GI Approximation

### Motion Blur 

Reference

Panel :

Properties ‣ Object Properties ‣ Motion Blur

Each object keeps its own motion blur settings beside the Scene Level Motion Blur.
You will find them under the Object Properties tab of the Properties.

Note

This bears only on the object's own motion. Switch it off and motion blur from elsewhere, camera movement or animated focal length say, stays put.

Steps
Rules deformation motion blur accuracy; more steps draw more memory.
The actual number of time steps is \(2^{steps -1}\) .

Deformation
Turns motion blur on for deformed meshes, animated characters and hair among them.

Warning

A modifier setup that shuffles mesh topology over time cannot render deformation motion blur right. Switch deformation blur off for such objects.
Animated Booleans, plus Deformation ahead of Edge Split, Remesh, Skin or Decimate modifiers, are the usual suspects.

### Shading 

Reference

Panel :

Properties ‣ Object Properties ‣ Shading

### Shadow Terminator 

Geometry Offset
Lifts rays off the surface to rein in shadow terminator artifacts on low-poly geometry.
Higher values reach more triangles, one touching them all and zero touching none.
The default reaches only triangles at grazing angles to light and should clear away most artifacts.

Unlike the Shading Offset , this barely sways the lighting, which makes it the better way to handle shadow terminator artifacts.

Shading Offset
Shoves the shadow terminator, the line parting lit from dark, toward the light to bury artifacts on low-poly geometry like the ones below:

| Description | Description |
| --- | --- |
| Shadow Terminator Artifacts.  | Result of using an offset of 0.15.  |

Note

This setting fakes a change to the scene's lighting; it neither conserves energy nor holds physically accurate (lean on Geometry Offset instead).

### Fast GI Approximation 

AO Distance
Overrides the world's AO Distance; set it to zero and the world's distance applies.

[Related references](INDEX.md).
