# Import/Export SVG as Grease Pencil

## Import/Export SVG as Grease Pencil

The Scalable Vector Graphics (SVG) format is used to trade vector-based illustrations between apps and is supported by vector editors such as Inkscape and by modern browsers, among others. Warning: the exporter runs only in Object Mode.

Import - Reference: menu: File ‣ Import ‣ SVG as Grease Pencil.
Resolution: the resolution for the generated strokes.
Scale: the generated strokes' scale.

Export - Reference: menu: File ‣ Export ‣ Grease Pencil as SVG.
Scene Options - Object: which objects to include. Active (only the active Grease Pencil object), Selected (all selected Grease Pencil objects), or Visible (all visible Grease Pencil objects in the scene).
Export Options:
Frame: which frames to include. Active (only the active keyframe), Selected (all selected keyframes as SVG animation), or Scene (all frames as SVG animation).
Sampling: the precision of stroke sampling; lower values give a more accurate result.
Fill: on, exports the Grease Pencil strokes' fill.
Uniform Width: on, exports strokes at a constant thickness.
Clip Camera: on (with camera view active), exports only the strokes clipped from camera view.
Note: the Grease Pencil strokes are always exported from the view of the current workspace's largest 3D Viewport.

[Related references](INDEX.md).
