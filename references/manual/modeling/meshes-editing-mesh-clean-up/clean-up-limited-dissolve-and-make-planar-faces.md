# Clean Up: Limited Dissolve, Make Planar Faces, Split Non-Planar Faces, Split Concave Faces

### Limited Dissolve 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Clean up ‣ Limited Dissolve

See Limited Dissolve.

### Make Planar Faces 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Clean up ‣ Make Planar Faces

Flattens the selected faces.

Factor
The flattening strength per iteration. Even 1 may fall short of perfectly flat — bump up the
Iterations if so.

Iterations
How many passes the operation runs.

### Split Non-Planar Faces 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Clean up ‣ Split Non-Planar Faces

Splits any selected faces bent past a given limit.

Max Angle
Faces bent by more than this angle get split.

Hint

You can use Rotate Edge if you'd rather have certain
newly created edges point in a different direction.

| Description | Description |
| --- | --- |
| Original mesh.  | Result of Split Non-Planar Faces.  |

### Split Concave Faces 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Clean up ‣ Split Concave Faces

Splits any selected concave faces until only convex ones are left.

| Description | Description |
| --- | --- |
| Original mesh.  | Result of Split Concave Faces.  |

[Related references](INDEX.md).
