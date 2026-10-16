# Introduction

Reference: Properties ‣ Modifiers

Grease Pencil features distinct modifiers. Modifiers perform automatic operations non-destructively. They let you apply effects that would otherwise require tedious manual work, without altering base geometry. Geometry Nodes can create custom Grease Pencil modifiers.

Modifiers change display and rendering but not editable geometry. Multiple modifiers stack on a single object; applying a modifier makes changes permanent.

Four modifier types exist: Edit—tools similar to Deform but affecting data like vertex groups rather than geometry directly. Generate—constructive tools that change appearance or add new geometry. Deform—shape changes without new geometry. Color—output color adjustments.

Interface: Each modifier shares fundamental interface components similar to mesh modifiers. See Modifiers Interface.

Applying Modifiers: Applying makes a modifier's effects permanent, converting strokes to match results and removing the modifier. Objects sharing data across multiple instances require Single User conversion, confirmed via pop-up.

Warning: Applying a non-first modifier ignores stack order, treating it as first; may produce unwanted results.

Reference: Properties ‣ Modifiers ‣ Modifier Header ‣ Specials

Apply (Active Keyframe): Ctrl + A—applies to current keyframe only. Apply (All Keyframes)—applies to all keyframes.

Note: Geometry Nodes can add layers; applying creates a single keyframe on frame one. Duplicated layer names deduplicate. Empty-name layers rename to Layer (Layer.001, etc. if needed).

Influence Filters: Most Grease Pencil modifiers share filtering options. Invert selection by clicking the icon beside each control. Layer/Group: Restricts to specified layer; click icon for layer-group filtering. Layer Pass: Restricts to matching Pass Index. Material: Restricts to specified material. Material Pass: Restricts to material matching Pass Index. Vertex Group: Restricts to assigned group. Custom Curve: Applies falloff curve controlling influence along stroke. Note: Filter availability depends on the specific modifier.

[Related references](INDEX.md).
