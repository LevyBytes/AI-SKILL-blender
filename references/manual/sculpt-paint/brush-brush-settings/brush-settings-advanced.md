# Brush Settings: Advanced

### Advanced

Brush Type
Defines the basic behavior and the available settings. Through the settings of a brush type, brushes can be created that produce vastly different effects.

The Essentials asset library contains brushes for each of the brush types. Their preview image and description should give a good idea of the effect the brush produces, with the particular combination of brush type and settings. Because of this, they are usually the more useful starting point for custom brushes than the mere brush type is, which is why the brush type is part of the Advanced brush settings.

Brushes and Brush Types of each mode:

- Sculpt

- Vertex Paint

- Weight Paint

- Texture Paint

Accumulate
Causes stroke dabs to accumulate on top of each other.

Front Faces Only
When enabled, the brush only affects vertices that are facing the viewer.

Affect Alpha 2D Painting Only
When this is disabled, it prevents changes to the alpha channel while painting (Only in 3D Viewport).

Anti-Aliasing 2D Painting Only
Toggles Anti-Aliasing around the brush, this is useful if you are working with pixel art or low resolution textures.

Auto-Masking Sculpt Mode
The auto-masking toggles in the brush settings are the same as the sculpt mode auto-masking settings. The difference is that these toggles can be customized per brush to create specific brush behaviors.

See also

For more information on the Auto-Masking toggles, see Auto-Masking.

Sculpt Plane Sculpt Mode
Use this menu to set the plane in which the sculpting takes place. In other words, the primary direction that the vertices will move.

Area Plane :

The movement takes place in the direction of average normal for all active vertices within the brush area. Essentially, this means that the direction is dependent on the surface beneath the brush.

View Plane :

Sculpting in the plane of the current 3D Viewport.

X, Y, Z Plane :

The movement takes place in the positive direction of one of the global axes.

Original Sculpt Mode

Normal
When locked it keeps using the normal of the surface where stroke was initiated, instead of the surface normal currently under the cursor.

Plane
When locked keep using the plane origin of surface where stroke was initiated, instead of the surface plane currently under the cursor.

[Related references](INDEX.md).
