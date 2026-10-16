# bpy.types.KinematicConstraint: limit_mode

limit_mode 

Which distances relative to the sphere of influence are permitted (default '`LIMITDIST_INSIDE`' )

- `LIMITDIST_INSIDE`
Inside – The object is constrained inside a virtual sphere around the target object, with a radius defined by the limit distance.

- `LIMITDIST_OUTSIDE`
Outside – The object is constrained outside a virtual sphere around the target object, with a radius defined by the limit distance.

- `LIMITDIST_ONSURFACE`
On Surface – The object is constrained on the surface of a virtual sphere around the target object, with a radius defined by the limit distance.

Type :

Literal[‘`LIMITDIST_INSIDE`’, ‘`LIMITDIST_OUTSIDE`’, ‘`LIMITDIST_ONSURFACE`’]

[Related references](INDEX.md).
