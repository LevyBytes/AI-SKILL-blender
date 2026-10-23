# Tracks

## Tracks

A track plays one or more actions in sequence, and you can make several tracks to play multiple actions simultaneously.

The track region offers these properties:
Disable NLA stack (checkbox in the blue object header) — unchecked, mutes every track but the Action Track.
Track name: double-click to change (not possible for the Action Track, which just shows the action's name).
Mute (checkbox in the gray track header) — unchecked, the track stops contributing to the animation and its strips get a dotted outline; individual strips can be muted too.
Lock (padlock icon): blocks changes to this track, handy when you want to move the strips in every track but a few.
Solo (star icon): mutes all other tracks, the Action Track included, so only this one drives the animation, which is useful for inspecting a track without distraction.

Action Track — the topmost track, with the orange header, holds the action being edited. Normally that's the object's active action, but selecting a strip and pressing Tab for Tweak Mode temporarily makes that one editable instead — in the Action Editor or the Graph Editor, say. The Action Track carries one of these buttons:
Push Down Action: unavailable in Tweak Mode; makes a new track below the Action Track and moves the active action there as a strip, leaving the Action Track empty (key something afterward and Blender auto-creates a new active action to hold it).
Pin: available only in Tweak Mode; unchecked, the action's keyframes appear at their original time points rather than the new ones produced by moving and scaling the strip.

[Related references](INDEX.md).
