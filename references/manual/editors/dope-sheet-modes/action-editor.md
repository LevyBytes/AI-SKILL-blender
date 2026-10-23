# Action Editor

## Action Editor

Where Dope Sheet mode works with the keyframes of every animation in the scene at once, Action Editor mode narrows to the keyframes within a single action.

Actions serve as Blender's containers for animation data; objects, like other animatable data-blocks, point at actions to be animated by the data they hold, a data-block can reference one action as its active action plus more through Nonlinear Animation tracks.

Header:
Note: the Previous/Next Layer (down/up arrow) operators were dropped from the UI in 4.4 and are slated for full removal in 5.0 (see #119626).
Action — a data-block menu for changing — or clearing — the object's active action.
Slot Display Name: the slot's name for display in the interface; combined with the slot's data-block type it stays unique inside its Action.

Action Menu:
Note: the "Merge Animation" and "Separate Slots" operators act only on directly-assigned actions and skip actions referenced by NLA strips.
Merge Animation — folds the animation of every selected object into the active object's animation. Because the data is moved rather than copied, the source Actions can wind up empty and userless. This merges not just the object-level Action but Actions on related data-blocks too (see Related data-blocks), so it can also merge the Actions of a single object — for example Translation & Rotation together with Shape Key animation.
Separate Slots: splits all Slots of the active object's Action into separate Actions; every user of those Slots is reassigned to its respective Action, and the new Actions take their names from the Slots. The source Action isn't deleted but may end with 0 users if no Fake User is set.
Replace Action — pops up so you can choose another action; the operator then finds all data-blocks using the active object's action and replaces it on each with your choice. This skips the action on NLA strips and action constraints — to replace those, see Remap Users.
Replace with New Action: makes a new Action (a duplicate of the current one) and points all users of the current Action at it. It ignores NLA Strips and Action Constraints.
Move Slots to new Action: moves the Slots selected in the Channels Region into a brand-new Action and reassigns all their users to it; with more than one Slot selected, they all go into a single Action.
Push Down Action: makes a new NLA track beneath the Action Track and shifts the active action into it, equivalent to hitting Push Down Action over in the NLA editor.
Stash Action: makes a new muted NLA track at the bottom of the NLA stack and shifts the active action there, effectively setting it aside and disabling it so it stops affecting the animation; later you can unmute it or delete it. Clicking New Action in an object's data-block menu when it already has an active action stashes the previous one automatically.
Note: both Push Down and Stash leave the object with no active action (so the Action Editor goes empty and the action can no longer be edited). To keep editing the action, pick it in the NLA editor and hit Tab to drop into Tweak Mode.

[Related references](INDEX.md).
