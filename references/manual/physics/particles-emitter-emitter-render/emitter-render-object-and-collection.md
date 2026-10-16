# Render: Object, Collection, Use Count, Extra

### Object 

Reference

Panel :

Particle System ‣ Render ‣ Object

Instance Object

Particles substitute this specified object.

Global Coordinates

References object world coordinates for instancing.

Object Rotation

Instances use object rotation.

Object Scale

Instances use object scale.

### Collection 

Reference

Panel :

Particle System ‣ Render ‣ Collection

Instance Collection

Group members get instanced consecutively at particle positions.

Whole Collection

All group members render simultaneously at each particle position rather than sequential selection.

Pick Random

Group members render in random sequence; only one appears per particle.

Global Coordinates

References object world coordinates for instancing.

Object Rotation

Instances use object rotation.

Object Scale

Instances use object scale.

#### Use Count 

Reference

Panel :

Particle System ‣ Render ‣ Collection ‣ Use Count

Allows individual objects within groups to render multiple times. The list view allows order and frequency specification.

Copy Particle Instance Object

Generates a duplicate of the list entry.

Remove Particle Instance Object

Strikes the entry from the list.

### Extra 

Reference

Panel :

Particle System ‣ Render ‣ Extra

Parents Particles

Incorporates parent particles when child particles get rendered. Children feature numerous deformation mechanisms, placing flat parent geometry behind their curved offspring. Parents hide automatically when Children activate. Refer to Children for details.

Unborn

Particles get rendered before generation.

Dead

Particles get rendered post-termination. Particularly helpful when particles expire at contact ( Die on hit ), allowing surface-based particle deposition.

[Related references](INDEX.md).
