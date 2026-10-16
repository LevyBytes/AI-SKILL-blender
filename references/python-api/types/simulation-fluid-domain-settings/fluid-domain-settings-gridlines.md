# bpy.types.FluidDomainSettings: gridlines_cell_filter, gridlines_color_field, gridlines_lower_bound, gridlines_range_color, gridlines_upper_bound

gridlines_cell_filter

Cell type to be highlighted (default 'NONE' )

- NONE
None – Highlight the cells regardless of their type.

- FLUID
Fluid – Highlight only the cells of type Fluid.

- OBSTACLE
Obstacle – Highlight only the cells of type Obstacle.

- EMPTY
Empty – Highlight only the cells of type Empty.

- INFLOW
Inflow – Highlight only the cells of type Inflow.

- OUTFLOW
Outflow – Highlight only the cells of type Outflow.

Type :

Literal[‘NONE’, ‘FLUID’, ‘OBSTACLE’, ‘EMPTY’, ‘INFLOW’, ‘OUTFLOW’]
gridlines_color_field

Simulation field to color map onto gridlines (default 'NONE' )

- NONE
None – None.

- FLAGS
Flags – Flag grid of the fluid domain.

- RANGE
Highlight Range – Highlight the voxels with values of the color mapped field within the range.

Type :

Literal[‘NONE’, ‘FLAGS’, ‘RANGE’]
gridlines_lower_bound

Lower bound of the highlighting range (in [-inf, inf], default 0.0)

Type :

float
gridlines_range_color

Color used to highlight the range (array of 4 items, in [0, inf], default (1.0, 0.0, 0.0, 1.0))

Type :

bpy_prop_array[float]
gridlines_upper_bound

Upper bound of the highlighting range (in [-inf, inf], default 1.0)

Type :

float

[Related references](INDEX.md).
