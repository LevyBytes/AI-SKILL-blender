# bpy.types.Brush: use_automasking_boundary_edges, use_automasking_boundary_face_sets, use_automasking_cavity, use_automasking_cavity_inverted, use_automasking_custom_cavity_curve, use_automasking_face_sets, use_automasking_start_normal, use_automasking_topology, use_automasking_view_normal, use_automasking_view_occlusion

use_automasking_boundary_edges

Leave non-manifold boundary edges untouched (default False)

Type :

bool
use_automasking_boundary_face_sets

Leave vertices on a face set boundary untouched (default False)

Type :

bool
use_automasking_cavity

Leave peak vertices untouched, judged by surface curvature (default False)

Type :

bool
use_automasking_cavity_inverted

Leave vertices inside crevices untouched, judged by surface curvature (default False)

Type :

bool
use_automasking_custom_cavity_curve

Apply a custom curve (default False)

Type :

bool
use_automasking_face_sets

Touch only vertices sharing face sets with the active vertex (default False)

Type :

bool
use_automasking_start_normal

Touch only vertices whose normal resembles the one where the stroke begins (default False)

Type :

bool
use_automasking_topology

Touch only vertices linked to the active vertex beneath the brush (default False)

Type :

bool
use_automasking_view_normal

Touch only vertices whose normal points toward the viewer (default False)

Type :

bool
use_automasking_view_occlusion

Touch only vertices that no other faces hide (slower performance) (default False)

Type :

bool

[Related references](INDEX.md).
