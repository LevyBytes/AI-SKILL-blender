# Metaball Properties

## Metaball Properties

All metas of the same family in a scene interact collectively. Settings in the Metaball section apply to the active family. When editing individual elements, the Active Element panel displays their per-element controls.

The Metaball panel in Object and Edit Mode contains family-level settings.

Viewport Resolution controls how fine the computed mesh appears in the 3D view, from finest to coarsest detail.

Render Resolution sets the mesh fineness used in final renders, also ranging from finest to coarsest.

As a visualization technique, lowering Resolution and raising Threshold while setting Stiffness just above Threshold reveals the mathematical directing structure underneath. A meta cube with Resolution at 0.410, Threshold at 5.0, and Stiffness at 5.01 clearly shows its underlying cubic core.

Influence Threshold defines the field strength at which the surface appears. Higher values increase the merging influence between metas. Influence can be positive (attraction, stretching toward each other) or negative (repulsion, pushing apart).

Update on Edit provides four visualization modes during transformation:

Always shows the full computed mesh during edits.

Half displays the mesh at half the viewport resolution while transforming.

Fast hides the mesh during manipulation.

Never suppresses mesh visibility entirely (only visible at render time—generally not recommended).

The Active Element panel controls individual meta properties visible in Edit Mode.

Type switches the element's underlying shape.

Stiffness determines the influence range of that specific element, controlling how readily it deforms when approached by other metas. Low values cause deformation from farther away; high values require closer proximity. The stiffness appears as a green ring and can be scaled directly.

The green ring must exceed the Threshold value to be visible.

Radius controls the element's physical size (equivalent to object-mode scaling). The white ring displays the radius and can be scaled.

Negative toggles whether the element attracts or repels neighboring metas.

Positive influence stretches surfaces toward each other as field boundaries overlap. Negative influence creates repulsion.

Note: negative-influenced metas are invisible in the viewport—only their boundary rings appear.

Hide conceals selected metas while disabling them from the field computation. This is useful for temporarily simplifying complex arrangements.

Boundary rings remain always visible in Edit Mode; selection circles appear in Object Mode.

[Related references](INDEX.md).
