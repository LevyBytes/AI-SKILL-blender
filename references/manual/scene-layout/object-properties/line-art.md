# Line Art

## Line Art

### Line Art

Reference

Mode :

Object Mode

Panel :

Properties ‣ Object Properties ‣ Line Art

The Line Art panel is used to enable extra display options for customizing Line Art rendering for a specific object.

Line Art panel.

Usage
How the object is loaded into Line Art. This property overrides the parent collection's Line Art usage.

Inherit :

No special loading strategy for Line Art. Loading of the object is controlled by parent collection's Line Art settings.

Include :

Force include the object into Line Art calculation even if its parent collection specifies otherwise.

Intersection Only :

The object will only produce intersection lines in the scene and its own geometry stays invisible.

Occlusion Only :

The object will only cause occlusion to existing feature lines and its geometry stays invisible.

Exclude :

The object will not be loaded into Line Art at all.

No Intersection :

The object will not generate intersection lines on itself or with other objects in scene.

Force Intersection :

Generate intersection lines even with objects that disabled intersection.

Override Crease
Allows the object to have a different crease value than the global one set in the Line Art modifier.

Crease
Override crease value for the object.

Intersection Priority
Assigns an intersection priority value for this object. The intersection line will be included into the object with the higher intersection priority value.

[Related references](INDEX.md).
