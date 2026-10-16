# Brush: Source

### Source

Reference

Type :

Brush

Panel :

Physics ‣ Dynamic Paint ‣ Source

Paint source panel. 

Paint source defines influence/intersection.

Mesh Volume

Brush affects points inside mesh volume.

Source: Mesh Volume. 

Proximity

Uses distance to brush mesh surface closest point. Interior isn't necessarily affected.

Source: Proximity. Brush affects surrounding canvas pixels. 

Mesh Volume + Proximity

Volume-type plus distance-based influence.

Inner Proximity
Applies proximity within volume.

Negate Volume
Inverts brush alpha inside volume.

| Volume + Proximity without extra settings.  | Inner Proximity shows proximity falloff inside volume.  |
| --- | --- |
| Negate Volume makes the volume interior transparent.  | Inner Proximity + Negate Volume combined.  |

Object Center

Instead of slow proximity-to-brush-mesh calculation, compute only center distance. Faster, usually adequate.

Source: Object Center. 

Particle System

Brush influence stems from selected particle system particles.

Effect Solid Radius
Solid-color paint distance.

Use Particle Radius
Adopts particle panel settings for solid radius. Disables manual Solid Radius.

Smooth Radius
Additional falloff radius beyond Solid Radius.

Zero Smooth Radius paints particles as solid spheres. Zero Solid Radius yields smooth halos.

Source: Particle System.

[Related references](INDEX.md).
