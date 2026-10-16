# Radial Tiling Node: Examples

### Examples

The Segment Coordinates output enables radially symmetric texture placement, shown by the radial heart texture tiling examples below.

| Description | Description |
| --- | --- |
| Sides: 5.0. | Sides: 6.5. |

Node tree for the shader above.

As section count increases, each section narrows, potentially causing texture overlap and clipping, evident in the Sides: 6.5 example. The non-integer value introduces additional clipping due to the smaller irregular section. To prevent this overlap, use the Segment Width output to scale textures proportionally to section size.

| Description | Description |
| --- | --- |
| Sides: 5.0. | Sides: 6.5. |

Node tree for the shader above. The value 0.725 is an arbitrarily chosen texture scaling value and can be adjusted to modify texture size.

By default, segment coordinate systems orient their Y-axes toward the center. Use the Segment Rotation output to align section coordinate systems with a global direction instead.

| Description | Description |
| --- | --- |
| Sides: 5.0. | Sides: 6.5. |

Node tree for the shader above. The value -1.571 is an arbitrarily chosen texture rotation value and can be adjusted to modify texture rotation.

When working with full-coverage textures, visible boundaries often appear along section borders despite seamless source textures. Enable Normalize to remove these boundaries by ensuring X-coordinates always span the full 0–1 range. This introduces distortion, which may need correction with additional nodes depending on artistic intent.

| Description | Description |
| --- | --- |
| Normalize: Disabled. | Normalize: Enabled. |

For certain textures, a softened appearance near section borders may be desirable, achievable by adjusting the Roundness input for segment coordinate systems.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Roundness: 0.0. | Roundness: 0.25. | Roundness: 0.5. | Roundness: 1.0. |

[Related references](INDEX.md).
