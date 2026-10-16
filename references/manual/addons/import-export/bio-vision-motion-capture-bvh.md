# BioVision Motion Capture (BVH)

## BioVision Motion Capture (BVH)

The BioVision Motion Capture (BVH) add-on moves .bvh data — a BioVision Hierarchical skeleton (rig) plus its animation — in and out of Blender through File ▸ Import/Export ▸ Motion Capture (.bvh); its usual job is pulling in mocap recordings. It ships enabled; otherwise switch on "BioVision Motion Capture (BVH) format" under Preferences ▸ Add-ons.

On import, Target decides interpretation: Armature for a rigged, animated skeleton (say a walk capture), or Object for a static mesh with no animation. The Transform group has Scale (enlarge the BVH physically), Rotation (its rotation order), and Forward/Up, which reconcile differing axis conventions — since tools disagree on which axis is "up," remapping converts rotations between their defaults. Blender treats Y as forward and Z as up (the front view sights down +Y), so a Y-up file usually wants -Z forward with Y up. The Animation group sets the Blender Start Frame for playback; Scale FPS, which retimes the file's rate to the scene (left off, one BVH frame equals one Blender frame); Loop for cyclic playback; plus options to push the scene's FPS and its duration to match the file.

On export, Transform again exposes Scale and Rotation; "Root Translation Only" limits written translation channels to the root bone; and Start/End picks the frame range to write.

[Related references](INDEX.md).
