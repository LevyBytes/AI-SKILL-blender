# Introduction

Sculpt Mode modifies drawing shape using a brush rather than individual elements; an area is altered using the brush's region of influence instead of selecting specific points.

**Sculpt Mode.**

Selected from the Mode menu in the 3D Viewport header. Once activated, the Toolbar changes to Sculpt Mode panels, and a red circle appears and follows the cursor in the 3D Viewport.

**Sculpting Options.**

Selection Mask — confines sculpting operations to picked points or strokes. Employ Toolbar selection tools for rapid selection; use Selection mode buttons to apply restrictions. Toggle modes via 1, 2, or 3.

Multiframe — sometimes simultaneous modification across multiple frames is needed. Activate the Multiframe control next to the modes selector (faded lines icon); consult Multiframe for guidance.

**Auto-Masking.**

Menu ‣ Header ‣ Auto-Masking; shortcut Shift+Alt+A. Automatically hides geometry per stroke, layer, and material beneath the cursor—shorthand for repetitive manual masking. Masks regenerate on each tool invocation and never render as visual overlays.

Access through Pie Menus via Shift+Alt+A. All auto-masking options compose, creating stricter masks.

Stroke — affects only the strokes under the cursor upon tool start.

Layer — affects only strokes belonging to the same layer as those under the cursor at tool start.

Material — affects only strokes sharing the material under the cursor at tool start.

Active Layer — affects only the current active layer's strokes.

Active Material — affects only strokes using the current active material.

**Keyboard Shortcuts.**

Invert stroke toggle — Ctrl.

Change active material — U.

[Related references](INDEX.md).
