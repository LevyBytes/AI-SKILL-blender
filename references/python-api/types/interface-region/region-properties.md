# bpy.types.Region: properties

active_panel_category 

The panel category currently active; this may be Null when the region lacks support for the feature (NOTE: these categories are built at runtime, so the list can be empty at initialization, before any drawing has happened) (default 'UNSUPPORTED' )

Type :

Literal[Region Panel Category Items]
alignment 

How the region is aligned inside the area (default 'NONE' , readonly)

- NONE
None – Don’t use any fixed alignment, fill available space.

- TOP
Top.

- BOTTOM
Bottom.

- LEFT
Left.

- RIGHT
Right.

- `HORIZONTAL_SPLIT`
Horizontal Split.

- `VERTICAL_SPLIT`
Vertical Split.

- FLOAT
Float – Region floats on screen, does not use any fixed alignment.

- `QUAD_SPLIT`
Quad Split – Region is split horizontally and vertically.

Type :

Literal[‘NONE’, ‘TOP’, ‘BOTTOM’, ‘LEFT’, ‘RIGHT’, ‘`HORIZONTAL_SPLIT`’, ‘`VERTICAL_SPLIT`’, ‘FLOAT’, ‘`QUAD_SPLIT`’]
data 

Data particular to the region (its type varies with the region type) (readonly)

Type :

AnyType
height 

The height of the region (in [0, 32767], default 0, readonly)

Type :

int
type 

Which type this region is (default 'WINDOW' , readonly)

Type :

Literal[Region Type Items]
view2d 

The region's 2D view (readonly, never None)

Type :

View2D
width 

The width of the region (in [0, 32767], default 0, readonly)

Type :

int
x 

Where the region sits vertically, relative to the window (in [-inf, inf], default 0, readonly)

Type :

int
y 

Where the region sits horizontally, relative to the window (in [-inf, inf], default 0, readonly)

Type :

int

[Related references](INDEX.md).
