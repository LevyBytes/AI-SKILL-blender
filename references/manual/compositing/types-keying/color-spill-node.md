# Color Spill Node

## Color Spill Node

The Color Spill node suppresses an unwanted color cast — usually green or blue — caused by light bouncing off a chroma-key screen onto the subject, a common compositing problem that gives an unnatural tint; the node reduces the chosen color channel's influence to restore a more natural look. Inputs: Image (the RGBA input to process); Factor (how strongly the node applies — 1.0 fully, lower values blending with the original); Spill Channel (which channel to reduce — R for red spill, G for green spill, common with green screens, or B for blue spill, common with blue screens); Limit Method (the reduction method — Simple, comparing the Limiting Channel to the others and reducing it where higher, or Average, using the average of the other two channels as the despill channel's limit); Limit Channel (Simple only — which channel(s) serve as the limiting reference: R, G, or B); and Limit Strength (the limit channel's strength). Spill Strength: when enabled, set the spill strength per color channel; when disabled, the spill channel uses a unit scale while the others are zero — with Strength setting each channel's spilling strength. Output: Image (the corrected image).

[Related references](INDEX.md).
