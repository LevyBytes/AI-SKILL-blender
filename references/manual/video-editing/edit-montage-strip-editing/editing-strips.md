# Video strips: Editing Strips

## Editing Strips

Transform — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Transform.
Move (G) — shifts the selected strips in time or onto a different track.
Extend (E) — quickly moves whichever selected strips sit on one side of the Playhead, handy when, say, you need to push everything after a certain time to the right to clear room. Select some or all strips, put the pointer left or right of the Playhead, press E, move the mouse to drag only the strips on that side, and confirm with LMB (or cancel with RMB). A strip straddling the Playhead has only its start or end moved, again depending on the pointer's side.
Scale (S) — scales the selected strips about the Playhead.
Swap — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Transform ‣ Swap; Shortcut: Alt-F. Swaps the order of the selected strips within their track.
Move Up — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Transform ‣ Move Up; Shortcut: PageUp. Moves the selected strips up a track when there's room.
Move Down — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Transform ‣ Move Down; Shortcut: PageDown. Moves the selected strips down a track when there's room.

Snap — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Snap.
Selection to Current Frame — moves the selected strips' start to the current frame.
Selection to Nearest Frame — moves their start to the nearest whole frame.
Selection to Nearest Second — moves their start to the nearest second.
Selection to Nearest Marker — moves their start to the nearest marker.

Split — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Split; Shortcut: Y. Cuts the selected strips in two at the current frame.

Duplicate — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Duplicate; Shortcut: Alt-D. Copies the selected strips, duplicating any actions they reference, so editing a copy's keyframes leaves the original untouched.

Linked Duplicate — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Linked Duplicate; Shortcut: Shift-D. Copies the selected strips while reusing the actions they reference, so editing a copy's keyframes also changes the original (and vice versa); Blender flags this by highlighting the other strip in red.

Delete — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Delete; Shortcut: Delete, X. Removes the selected NLA-Strips.

Make Meta — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Make Meta; Shortcut: Ctrl-G. Groups the selected NLA-strips into a meta strip.

Remove Meta — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Remove Meta; Shortcut: Ctrl-Alt-G. Ungroups the selected meta strips, putting their contents back in place.

Toggle Muting — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Toggle Muting; Shortcut: H. Mutes or unmutes the selected strips; muted ones get a dotted border and stop affecting the animation.

Bake Action — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Bake Action. Also Reference: Editor: 3D Viewport; Mode: Object and Pose Modes; Menu: Header ‣ Object ‣ Animation ‣ Bake Action…. An object's or bone's final motion comes not only from keyframed animation but also from F-Curve modifiers, drivers, and constraints; Bake Action computes that final motion and lays down a keyframe on every scene frame. It's handy for adding variation to a cyclic action like a Walk Cycle, or for turning drivers or constraints into keyframe animation.
  Start Frame — the first frame to bake.
  End Frame — the last frame to bake.
  Frame Step — how many frames to skip ahead between baked frames.
  Only Selected Bones — keys only the selected bones (Pose baking only).
  Visual Keying — keys from the final transformations, with constraints applied.
  Clear Constraints — strips all constraints from the keyed objects/bones and does "visual" keying.
  Clear Parents — bakes the animation onto the object then clears parents (objects only).
  Overwrite Current Action — bakes into the current action rather than a new one (handy for baking only some bones of an armature).
  Clean Curves — removes redundant keys after baking.
  Bake Data — which transforms to bake: Pose (bone transforms) or Object (object transforms).
  Channels — which channels to bake: Location, Rotation, Scale, B-Bone, or Custom Properties.

Apply Scale — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Apply Scale; Shortcut: Ctrl-A. Bakes the selected strips' scale into their referenced actions.

Clear Scale — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Clear Scale; Shortcut: Alt-S. Resets the selected strips' scale.

Sync Action Length — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Sync Action Length. Resets a strip's length to its underlying action's, so it plays only from the action's first keyframe to its last. See also the Sidebar's Sync Length Now button, which does the same.

Make Single User — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Make Single User; Shortcut: U. Duplicates actions as needed so each selected strip gets its own action used by no others, letting you edit a strip's keyframes without touching the rest of the animation.

Note: this doesn't recurse into meta strips.

Start Editing Stashed Action — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Start Editing Stashed Action; Shortcut: Shift-Tab. Enters Tweak Mode for the selected strip's action so its keyframes can be edited in, e.g., the Graph Editor, and marks the strip's track as Solo, muting every other track so they stop influencing the animation and you can focus solely on the action at hand. Despite the name's "stashed (muted)" wording — which just reflects the usual case — it works on unmuted actions too. When done, click Strip ‣ Stop Editing Stashed Action or press Shift-Tab again.

Start Tweaking Strips Actions (Full Stack) — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Start Tweaking Strips Actions (Full Stack); Shortcut: Tab. Enters Tweak Mode for the selected strip's action so its keyframes can be edited, leaving every other track on so you still see their effects while you work. When done, click Strip ‣ Stop Tweaking Strips Actions or press Tab again. Note: for transitions sitting above the tweaked strip, keyframe remapping breaks down for any channel values the transition affects; the way around it is to tweak the active strip while skipping evaluation of the upper NLA stack.

Start Tweaking Strips Actions (Lower Stack) — Reference: Editor: Nonlinear Animation; Menu: Strip ‣ Start Tweaking Strips Actions (Lower Stack). Enters Tweak Mode for the selected strip's action so its keyframes can be edited, muting any tracks above the current one so they don't influence the animation while you work. When done, click Strip ‣ Stop Tweaking Strips Actions or press Tab.

[Related references](INDEX.md).
