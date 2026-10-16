# Custom Properties

## Custom Properties

Custom properties let you stash your own data in Blender's data-blocks. They're handy for rigging (bones and objects can carry custom properties that drive other properties) and for Python scripts, where it's common to define settings Blender doesn't have; you can also reach them from materials via the Attribute Node. Only certain data supports them: every data-block type, bones and pose bones, and sequence strips. To add one, find the Custom Properties panel at the bottom of most Properties or Sidebar regions and click New; remove them from the same spot with the delete icon, and once added, configure them with the edit icon for a given use case (see Editing Properties).

Editing Properties — User Interface: custom properties are edited through the panel on data types that support them, where you set things like default values, ranges, and even a custom tooltip.
Type — the property's data type; each type allows only certain data settings.
  Float — a number with decimals, e.g. 3.141, 5.0, or 6.125.
  Float Array — several floats together, e.g. [3.141, 5.0, 6.125]; it also suits data representable as a float array, like colors, which you set via the Subtype selector.
  Integer — a number with no decimals, e.g. 1, 2, 3, or 4.
  Integer Array — several integers together, e.g. [1, 2, 3, 4].
  Boolean — two possible values, e.g. True or False.
  Boolean Array — several booleans together, e.g. [True, False, True].
  String — a run of characters such as "Some Text".
  Data-Block — a reference to a Blender object (see Data-Blocks).
  Python — edit a Python data type directly, for unsupported types.
Array Length — how many elements the array holds; above 7, you can't edit elements directly and must press Edit Value to do so.
Property Name — the text shown to the left of the value, also the key used to reach the property from Python.
Default Value — the property's default, used by the Reset to Default Value operator. Warning: default values seed NLA blending, so a nonsensical default (0 for a scaling property, say) on a property meant for keyframing is likely to cause trouble.
Min, Max — the smallest/largest value the property may take.
Library Overridable — lets the property be overridden when the data-block is linked.
Soft Limits — caps how far the Property Value slider reaches without typing the value in.
Soft Min, Max — the soft limit's smallest/largest value.
Step — a multiplier for how much the value changes per increment; the internal float step is 0.01, so a Step of 5 increments by 0.05 and a Step of 100 by 1.0, while the internal integer step is 1.
Precision — how many digits after the decimal show in the UI for float types.
Subtype — what kind of data the property holds, which shapes its UI; available only for float properties, with different choices for regular floats and float arrays (the unit often follows the Scene Units).
  For regular floats: Plain Data (no special behavior), Pixel (a digital-image-resolution measure), Percentage (shown as a percentage, usually with Min/Max of 0 and 100), Factor (a percentage between a lower and upper bound with numerical meaning), Angle (a measure between intersecting lines), Time (seconds), Distance (a measure of space between items), Power (work over time, in watts — Blender uses it for light intensity), Temperature (how much heat is present), Wavelength (the distance between wave cycles, in mm, µm, nm, or pm).
  For float arrays: Plain Data (no special behavior), Linear Color (color in linear space), Gamma-Corrected Color (color in gamma-corrected space), Euler Angles (Euler rotation angles), Quaternion Angles (Quaternion rotation angles).
  Note: for either color subtype to behave, the Property Value must be a vector of three or four values, depending on whether there's an Alpha Channel.
ID Type (Data-Block) — the ID-block type, e.g. Key, Image, Object, Material; see Data-Block Types for the full list.
Description — lets you write a custom Tooltip for the property.

Python Access — custom properties are reached much like dictionaries, with the catch that a key must be a string, while a value must be a string, a number, an array of those, or a nested property. See the API documentation for details.

[Related references](INDEX.md).
