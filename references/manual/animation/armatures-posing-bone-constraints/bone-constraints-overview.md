# Introduction

Because bones behave like objects in Pose Mode, they can be constrained, which is why the Constraints tab appears in Object and Edit Mode; the panel holds the active bone's constraints (its name shown at the top in the "To Bone:…" field). Constraining bones can limit their pose-transform freedom (for example with the Limit constraints), make a bone track another object or bone (in the same armature or another), and so on — and inverse kinematics is mainly available through the IK Solver constraint, which is bone-specific. For instance, a human elbow can't rotate backward (barring injury) or sideways, and its forward and roll rotations are bounded (perhaps 0 to 160, or -45 to 135, depending on the rest pose), so you'd apply a Limit Rotation constraint to the forearm bone (since elbow motion comes from rotating the forearm around its root). Using bones in constraints, as owners or targets, is detailed in the constraints pages.

[Related references](INDEX.md).
