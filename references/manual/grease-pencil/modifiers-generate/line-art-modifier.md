# Line Art Modifier

## Line Art Modifier

Line Art is a modifier that derives stylized strokes by tracing geometry drawn from a whole scene, a chosen collection, or one isolated object. An active camera is required, because only the geometry visible from that camera's viewpoint will yield lines.

Note: Currently, each Line Art modifier independently executes full occlusion calculation. Using multiple modifiers (for varying styles) significantly increases compute time. Future improvements are planned.

Use Cache: Speeds up rendering by reusing cached scene data from the first Line Art modifier, at the cost of restricting certain settings. Available only with multiple Line Art modifiers when the current modifier is not first.

Source Type: Specifies geometry source. Scene uses all visible objects. Collection uses objects in a chosen collection. Object generates from a single object (supported types: Mesh, Text, Curve, Surface, Curves).

Object/Collection: Selects source based on type. Invert Collection Filtering: Selects everything except lines from specified collection.

Note: Line Art loads and processes the entire visible scene for correct occlusion, unless configured differently in object or collection Line Art Usage.

Layer: Grease Pencil layers receiving results. Material: Grease Pencil materials for strokes. Line Radius: Stroke width. Opacity: Stroke opacity.

Edge Types: Line Art recognizes multiple edge categories. Selected types appear in output.

Illumination Filtering: Filters feature lines by lighting. None—no filtering. Illuminated—only lit-region lines. Shaded—only shaded-region lines. Illuminated (Enclosed Shapes)—lit-region lines, with contour/light-contour/shadow combined into closed forms.

Create: Contour generates lines where front/backfacing faces separate; inversible. Contour shows surface contours. Silhouette shows object outline. Individual Silhouette shows each object's contour separately. Crease generates lines at sharp angles. Crease Threshold: Angle below which treated as crease (object override takes precedence). Intersections: Lines where faces meet. Material Borders: Lines separating different-material faces. Edge Marks: Lines from freestyle marks. Loose: Unpaired edges. Light Contour: Light/shadow boundaries from a light. Cast Shadow: Light-projected contour lines. Allow Overlapping Types: Multiple types per edge create separate strokes.

Light Reference: Light Object for Light Contour. Shadow Camera Size: Orthographic scale of shadow camera. Near/Far: Shadow camera clipping.

Geometry Processing: Custom Camera uses alternate camera instead of active. Overlapping Edges as Contour: Overlapped edges (e.g., split modifier or imported coincident edges) render as contour; slightly slower but handles overlap correctly. Instanced Objects: Loads particles/instanced objects; performance impact with many instances. Clipping Boundaries: Generates clipping contours at near/far plane intersections. Crease on Smooth: Crease edges visible in smooth surfaces. Crease on Sharp: Creases show on sharp edges. Force Backface Culling: Removes back faces to accelerate; changes occlusion levels.

Occlusion: Range (when enabled) selects lines within start/end occlusion levels. Level: Desired occlusion—0 means fully visible; 1 means occluded by one face layer.

Material Mask: Selects lines occluded by faces with specific masks. Masks: Matching bits. Exact Match: All bits must match, or any one.

Intersection: Allows edges between two collections. Collection Mask: Bits from Collection properties. Exact Match: All masks required.

Face Mark Filtering: Manual control using Freestyle marks. Invert: Reverses filter. Boundaries: Lines at mark edges. Keep Contour: Preserves contours during filtering.

Chaining: Chain: Intersection with Contour links intersection lines with contours. Note: Ambiguity may result; unchained intersections remain separate. All Lines: All lines treated as contour and chained. Loose Edges: Floating edges chain together. Loose Edges as Contour: Unpaired edges classified as contours. Preserve Details: Small details maintain across occlusion; omitting creates smoother results. Geometry Space: Uses geometry distance instead of image-space. Image Threshold: Short segments chain if 2D distance is within threshold. Smooth Tolerance: Smoothing strength on jagged sequences. Angle Splitting: Breaks chains at sharp turns above angle.

Vertex Weight Transfer: Filter Source: Vertex groups prefixed with this text transfer weights. Match Output: Transfers filtered weights to identically-named Grease Pencil groups. Target: Alternate group when Match Output is off; highest weight copied if multiple.

Composition: Overscan: Margin outside camera view prevents strokes ending abruptly; Blender only renders visible edges as an optimization. Image Boundary Trimming: Cuts strokes at image edge. Depth Offset: Shifts strokes toward camera, avoiding clipping; unavailable if Show in Front is enabled. Towards Custom Camera: Offsets toward selected camera.

Bake: Bake Line Art: Records Line Art strokes within start/end range; deactivates afterward. Bake All: Records all Grease Pencil objects with modifiers. Clear Baked Line Art: Clears recorded frames in range. Clear All: Clears all recorded.

Warning: Manual strokes drawn in the bake range also clear.

Continue without Clearing: Re-activates a modifier without clearing, useful for multi-section work.

Demonstration of material masks in action. Intersection: Edges can be selected where two collections meet. Collection Mask: Mask bits matched from Collection properties. Exact Match: Requires all intersection masks match instead of any one.

Demonstration of collection masks in use. Face Mark Filtering: Manual edge selection via Freestyle marks. Face Mark Filtering subpanel. Invert: Reverses the filter. Boundaries: Filters feature lines based on face-mark borders. Keep Contour: Retains contours during filter application.

Chaining: Line chaining merges nearby segments. Chaining subpanel. Chain: Intersection with Contour—intersection lines can merge with nearby contours. Note: Enabling creates ambiguity; unmerged intersections remain separate. All Lines—all become contour type and merge. Loose Edges—floating edges merge together. Loose Edges as Contour—unpaired edges become contour. Preserve Details—maintains small details rather than splitting at each occlusion change; omitting creates smoother output. Geometry Space—uses geometry distance instead of image-space distance. Image Threshold: Distance below which segment endpoints chain together. Smooth Tolerance: Smoothing applied to jagged chains. Angle Splitting: Chains separate at turn angles exceeding this value.

Vertex Weight Transfer: Weight data flows from source mesh to strokes. Vertex Weight Transfer subpanel. Filter Source: Vertex groups prefixed with this text transfer. Match Output: Copies filtered weights into Grease Pencil groups with identical names. Target: Assigned group when Match Output is off; uses highest weight if multiple.

Composition: Rendering optimizations. Composition subpanel. Overscan: Margin prevents stroke cutoff; without it, Blender only renders visible edges. Image Boundary Trimming: Clips strokes at image limits. Depth Offset: Camera-ward shift prevents z-clipping while maintaining depth; unavailable with Show in Front. Towards Custom Camera: Offsets toward selected camera instead of active.

Bake: Recording and management. Bake options. Bake Line Art: Records within start/end range; auto-disables. Bake All: Records all Grease Pencil objects containing modifiers. Clear Baked Line Art: Removes recorded frames in range. Clear All: Removes all recorded.

Warning: Manual strokes in the bake range also delete.

Continue without Clearing: Reactivates without clearing—helpful for sectioned work.

[Related references](INDEX.md).
