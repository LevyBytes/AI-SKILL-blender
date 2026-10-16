# Fill Tool: Advanced, Gap Closure

#### Advanced

Boundary
Chooses how the fill boundary limits get computed.

All :

Combine stroke thickness with the editing lines.

Strokes :

Lean on stroke thickness alone, ignoring edit lines.

Edit Lines :

Lean on the edit lines alone, ignoring strokes.

Show Lines (eye icon)
Flip on helper lines that reveal the fill boundary.

Layers
Picks which Layers supply the boundary strokes.

Visible :

Derives boundaries from every visible layer.

Active :

Derives boundaries from the active layer.

Layer Above :

Derives boundaries from the layer just above the active one.

Layer Below :

Derives boundaries from the layer just below the active one.

All Above :

Derives boundaries from every layer above the active one.

All Below :

Derives boundaries from every layer below the active one.

Simplify
How many simplify steps run on the boundary line; higher counts cut the precision of the filled region.

Ignore Transparent
Switch this on and transparent strokes are left out of the boundary math.

A value slider sets where the transparency threshold falls for a material.

Limit to Viewport
Switch this on and the fill reaches only the viewport's visible regions.

Auto-Remove Fill Guides
Switch this on and the guide strokes clear themselves away once a fill lands.

##### Gap Closure
Temporary lines spawned automatically to seal up gaps left in the strokes.

Size
Length of the extension line, or the circumference feeding the gap-closing calculation.

Mode S
Chooses which Gap closure method runs.

Radius :

Works out a closing line from the circle radius around the nearest open points.

Extend :

Stretches the open strokes out to bridge gaps.

Visual Aids
Flip on the closure-line helper display.

Strokes Collision D
Watches for extension lines hitting strokes and halts the extension at the first collision.

[Related references](INDEX.md).
