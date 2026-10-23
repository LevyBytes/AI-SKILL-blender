# Strips

## Strips

A strip says when something happens in the animation and for how long. A few types exist, described below.

Action Strips: this kind of strip plays back the keyframes held in an action. Create one with Add ‣ Action, or by clicking Push Down Action in the NLA's Action Track, which builds a strip from the object's active action. Several strips can reference the same action, so editing one set of keyframes can change multiple parts of the animation at once. A strip may be shorter than its underlying action (by cropping, speeding up, or both) or longer (by extending, slowing down, or both); see the Sidebar for details.

Transition Strips: a transition strip interpolates between two neighboring action strips: select them and click Add ‣ Transition.

Sound Strips: these control when a Speaker Objects begins playing its audio; playback runs the length of the audio file and ignores the sound strip's length.

Meta Strips: a meta strip bundles other strips so you can move, scale, and copy them as one unit.

[Related references](INDEX.md).
