# Cameras: Viewport Display, Composition Guides

### Viewport Display 

Camera view displaying safe areas, sensor and name. 

Size
The camera's drawn size in the 3D Viewport. This touches nothing in the render output. The standard Scale S transform key resizes the camera visualization too.

Show

Limits
Draws an orange line marking Clip Start and End, plus a yellow cross at the Focus Distance .
With the Focus Distance gizmo switched on in the 3D Viewport's gizmo settings, you can drag that cross by mouse to set the distance.

Mist
Flips the mist-limit display on or off.
Two joined white dots along the camera sightline mark them.
You set the mist limits and their companion options over in the World panel's Mist section.

Sensor
Puts a dotted frame inside camera view.

Name
Flips the name display on or off in camera view.

Passepartout
Dims everything beyond the camera's field of view.
The value slider sets how opaque that dimming runs.

Tip

A fully opaque Passepartout lets Blender optimize, speeding up rendering of the area within the camera view.

#### Composition Guides 

Turn on Composition Guides to lay framing aids over the camera display.

Thirds
Rules the frame into vertical and horizontal thirds.

Center

Center
Rules the frame into vertical and horizontal halves.

Diagonal
Joins the opposite corners with lines.

Golden

Ratio
Splits width and height by Golden proportions (close to 0.618 of the size in from each frame edge).

Triangle A
Strikes a diagonal from lower-left up to upper-right, then drops perpendiculars passing through the corners at top-left and bottom-right.

Triangle B
As A, swapped to the other corner pair.

Harmony

Triangle A
Strikes a diagonal from lower-left up to upper-right, then sends lines from each of the bottom-right and top-left corners out to 0.618 along the facing side.

Triangle B
As A, swapped to the other corner pair.

Color
Fixes the color and opacity (alpha) every composition guide overlay shares.
Useful for dialing their visibility up or down against a lighter or darker shot.

[Related references](INDEX.md).
