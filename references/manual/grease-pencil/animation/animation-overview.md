# Introduction

### Introduction

### Animating with Grease Pencil

Grease Pencil exists to bring a 2D animation toolset fully inside a 3D environment.

Sample animation showing Grease Pencil object keyframes in the Dope Sheet with onion skinning enabled.

Several animation routes are open to Grease Pencil objects in Blender:

Moving as a whole object
Shifting the object's position, orientation, or size over time;

Drawing frame by frame
Hand-drawing a single frame at a time, the traditional approach.

Deforming them
Animating the underlying points;

Inherited animation
Letting one object ride along on another object's motion (a parent, hook, armature, and so on). Handy for cut-out animation, among other uses.

The Animation & Rigging chapter gives the full picture of animation in Blender.

### 2D Traditional Animation

### Keyframes
Traditional Grease Pencil animation runs on keyframes, each storing the stroke data for one frame or a span of frames.

Turn Auto keyframe on, and drawing a stroke in a Grease Pencil object's Draw Mode drops a new keyframe at the current frame on the active channel. Turn it off, and you either add a keyframe by hand or your new strokes pile onto the active keyframe.

Keyframe Editing has the details.

Note

A Dope Sheet channel maps to the active 2D layer of the Grease Pencil object.

For keyframe work, Grease Pencil supplies its own Dope Sheet mode; the Grease Pencil mode in the Dope Sheet section explains it. The Stroke menu also carries several keyframe-and-stroke tools, documented under Animation tools.

### Onion Skinning
Onion skinning is a staple of traditional animation, and Grease Pencil packs plenty of flexibility and settings into the feature. Onion Skinning covers it.

### Animation Options

### Draw Mode
Draw Mode exposes three animation-related options to work with.

General drawing/animation options.

Add Weight Data
Switch this on and fresh strokes pick up weight data from the active vertex group and its weights. With no vertex group chosen, no weight data is written.

Cut-out animation benefits here, for instance, letting you add a drawing onto the same vertex group without having to build it afterward.

Weight Paint Mode has more.

Additive Drawing
On a new frame, the strokes from the previous or active frame carry over as a foundation for the new one.

Multiframe
To paint new strokes across several frames of your animation, switch on multiframe drawing.

Toggle it with the Multiframe button beside the modes selector (the faded-lines icon). Multiframe has more.

### Edit Mode
Edit Mode offers one animation-related option.

Multiframe editing.

Multiframe
At times you need to tweak several frames together with the edit tools, say to reposition drawings throughout an animation.

Turn on multiframe editing with the Multiframe button beside the modes selector (the faded-lines icon). Multiframe has more.

### Examples

[Related references](INDEX.md).
