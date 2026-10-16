# bpy.types.PoseBone: bbone_curveinx, bbone_curveinz, bbone_curveoutx, bbone_curveoutz, bbone_custom_handle_end, bbone_custom_handle_start, bbone_easein, bbone_easeout, bbone_rollin, bbone_rollout, bbone_scalein, bbone_scaleout

bbone_curveinx

Curvature handle offset along X at the B-Bone curve's start (in [-inf, inf], default 0.0)

Type :

float
bbone_curveinz

Curvature handle offset along Z at the B-Bone curve's start (in [-inf, inf], default 0.0)

Type :

float
bbone_curveoutx

Curvature handle offset along X at the B-Bone curve's end (in [-inf, inf], default 0.0)

Type :

float
bbone_curveoutz

Curvature handle offset along Z at the B-Bone curve's end (in [-inf, inf], default 0.0)

Type :

float
bbone_custom_handle_end

The bone acting as the end handle of the B-Bone curve (readonly)

Type :

PoseBone
bbone_custom_handle_start

The bone acting as the start handle of the B-Bone curve (readonly)

Type :

PoseBone
bbone_easein

Length of the first Bézier Handle (B-Bones only) (in [-inf, inf], default 0.0)

Type :

float
bbone_easeout

Length of the second Bézier Handle (B-Bones only) (in [-inf, inf], default 0.0)

Type :

float
bbone_rollin

Twist applied via roll offset at the B-Bone's start (in [-inf, inf], default 0.0)

Type :

float
bbone_rollout

Twist applied via roll offset at the B-Bone's end (in [-inf, inf], default 0.0)

Type :

float
bbone_scalein

Thickness scale factors at the B-Bone's start, for tapering (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

Type :

mathutils.Vector
bbone_scaleout

Thickness scale factors at the B-Bone's end, for tapering (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

Type :

mathutils.Vector

[Related references](INDEX.md).
