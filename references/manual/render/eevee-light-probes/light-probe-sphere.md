# Light Probe Sphere

## Light Probe Sphere

### Light Probe Sphere

A spherical light probe records incoming light from many angles at one location.

Application targets smooth and semi-rough reflections. Sphere probes transition smoothly toward volumetric lighting for purely diffuse cases.

With raytracing active, they act as missed-ray fallback.

Note

Light probe volumes overshadow sphere probes, minimizing light leakage in shadowed areas and reducing needed setup.

Adjustment occurs in Scene data panel.

World carries an inbuilt sphere probe with adjustable resolution in World data panel.

### Properties

Reference

Panel :

Object Data ‣ Probe

Type
Influence volume shape: Sphere or Box.

Radius / Size
Probes alter nearby surface lighting. Size and scaling define influence extent.

Falloff
Influence fade percentage within the distance.

### Capture

Note

Viewport capture happens upon detected probe or position update. Frame rendering captures at start.

Clipping Start, End
Near and far clip for scene capture.

### Custom Parallax

Reference

Panel :

Object Data ‣ Custom Parallax

Standard: influence volume equals parallax volume. Parallax volume projects captured light, matching surroundings. Custom Parallax enables independent parallax adjustment.

### Viewport Display

Data
Show captured light as a reflective sphere at given size.

Clipping
Show capture clip distance.

Influence
Show influence bounds. Inner sphere marks falloff start.

Parallax
Show Custom Parallax shape.

[Related references](INDEX.md).
