# Bone Structure

## Bone Structure

A bone has three elements: the start joint (root or head), the body, and the end joint (tip or tail). With that default armature in Edit Mode, the root and tip can be selected and moved just like mesh vertices; together these joints define the bone by their positions, and they each carry a radius property used only by the envelope deformation method. Roll: enabling the Axes checkbox shows each bone's local axes at its tip, where the Y axis always runs along the bone from root to tip — the bone's roll axis. Bone influence: a bone controls geometry when vertices "follow" it, much as a finger's muscles and skin follow the finger bone, which requires defining how strongly a bone influences a given vertex. The simplest approach has each bone affect the geometry within a set range of it — the envelope technique, since each bone controls only the geometry "enveloped" by its influence area. When a bone is shown as Envelope, in Edit and Pose Mode you can see that influence area, which depends on the Distance property and the root and tip radii; these parameters are detailed further in the skinning pages.

[Related references](INDEX.md).
