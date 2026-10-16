# Bone Info Node

## Bone Info Node

### Bone Info Node

The Bone Info node retrieves bone transform data from an armature object. Useful for rig-driven geometry control or implementing skeletal deformation via vertex-group attributes.

Note: A dependency cycle can occur if the node references one bone while another bone in the same armature depends on the modified object (e.g., via a Geometry Attribute Constraint). The modifier can only add a dependency on the entire armature, not individual bones, because the bone name is a generic string.

### Inputs

Armature
Source armature object for bone pose data.

Bone Name
Name of the bone whose pose transforms to retrieve.

### Properties

Transform Space
Coordinate system for pose output.

Original:
Output pose and rest pose relative to armature origin.

Relative:
Project pose and rest pose into the modified object's space.

### Outputs

Pose
The bone's evaluated final transform.

Local Pose
Pose minus rest pose, relative to the parent bone. Not affected by transform space.

Transform Pose
Matrix encoding the bone's location, rotation, and scale. Not affected by transform space.

Rest Pose
The bone's original transform (edit-mode definition).

Rest Length
The bone's original length.

[Related references](INDEX.md).
