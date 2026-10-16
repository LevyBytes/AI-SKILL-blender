# Copy/Paste Pose

## Copy/Paste Pose

Copy/Paste Pose (Pose Mode; Pose ‣ Copy Pose / Paste Pose / Paste Pose Flipped; Ctrl-C / Ctrl-V / Shift-Ctrl-V): copy and paste a pose via the menu or hotkeys — Copy Pose puts the selected bones' current pose in the pose buffer, Paste Pose applies the buffer to the posed armature, and Paste Pose Flipped applies the X-mirrored buffer. Key points: it works at the Blender-session level, so you can use it across armatures, scenes, and files, but the buffer isn't saved (lost on quitting Blender); there's only one buffer; only selected bones are copied; on pasting, selection doesn't matter and the pose applies per bone name (so a copied forearm pose goes to the destination's forearm bone, and nothing happens if no such name exists); and what's actually copied is each bone's position, rotation, or scale in its own space, so the pasted result can differ markedly from the original depending on the bones' rest positions and their parents' current poses.

[Related references](INDEX.md).
