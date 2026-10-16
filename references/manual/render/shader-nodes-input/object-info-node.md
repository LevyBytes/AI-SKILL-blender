# Object Info Node

### Object Info Node

Access object instance data to vary a single material across multiple instances—via object index, location, or randomization. For example, pair with a Noise texture for random colors or a Color Ramp for color selection.

### Inputs

None.

### Properties

None.

### Outputs

- **Location** — Object position in world space.
- **Color** — Object color (same as Viewport Display ‣ Properties ‣ Object Properties ‣ Color).
- **Alpha** — Alpha Channel component of viewport display color (see Color output).
- **Object Index** — Pass Index (same as Properties ‣ Object Properties ‣ Relations ‣ Pass Index).
- **Material Index** — Pass Index (same as Properties ‣ Material ‣ Settings ‣ Pass Index).
- **Random** — Float between 0.0–1.0 unique to each object instance.

Note: This node works only for material shading nodes, not light or world shaders.

### Example

Example blend-file.

[Related references](INDEX.md).
