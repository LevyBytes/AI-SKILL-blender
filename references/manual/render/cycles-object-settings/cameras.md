# Cameras

### Cameras 

### Panoramic Cameras 

Cycles carries several panoramic camera types, each laid out below.
Note that none of them can show in non-rendered viewport modes, Solid mode among them; they kick in only for the final render.

### Equirectangular 

Render the scene as a panorama from the camera's spot using an equirectangular projection, always sweeping the full 360° on the X axis and 180° on the Y axis.

Since this projection agrees with the environment texture world shaders use, you can render an environment map with it. For the default mapping, give the camera object a rotation of (90, 0, -90), or simply aim it down the positive X axis.
That comes to looking at the image center under the default environment texture mapping.

Latitude Min, Max
Bounds on the vertical field of view angles.

Longitude Min, Max
Bounds on the horizontal field of view angles.

### Equiangular Cubemap Face 

A step up from Equirectangular, spreading the rendered pixels of the spherical environment more evenly.
The payoff is an image whose visual resolution scarcely budges across the whole spherical projection.
Equirectangular, by contrast, can bleed detail at the poles, and cube map projections bleed it near each face's edges.

This panorama type shines for virtual reality, where wringing the most visual detail out of a capped resolution matters.

One thing it gives up against Equirectangular is any longitude or latitude limits.

### Fisheye 

Fisheye lenses run wide angle with heavy distortion, useful for panoramic images bound for dome projection say, or for an artistic flourish.

For the closest match to real cameras, reach for the Fisheye Equisolid lens.
It hands you a focal length together with a field-of-view angle, and the sensor dimensions feed in as well.

The Fisheye Equidistant lens maps to no real lens model; it throws a circular fisheye that pays the sensor information no mind and instead works the whole sensor. That makes it a fine lens for full-dome projections.

Lens
The lens's focal length, given in millimeters.

Field of View
The field-of-view angle; push it to 360 and beyond to swallow the whole environment.

### Fisheye Lens Polynomial 

Pin down a real-world camera by handing over the coefficients of a degree-four polynomial.

Here is the projection's chain of steps.
Every image pixel finds a spot \((x, y)\), measured in mm, across the camera sensor.
From that sensor spot follows a direction whose spherical coordinates run
\((1, \theta, \phi)\), in radians, this way:

\[\begin{split}& r = \sqrt{x^2 + y^2}\\
& \theta = k_0 + k_1 r + k_2 r^2 + k_3 r^3 + k_4 r^4\\
& \phi = acos(x/r)\end{split}\]

Light coming in along that direction then lands on the matching pixel.

You can model both fisheye and perspective cameras this way.

### Mirror Ball 

Render as if photographing a reflective mirror ball.
On rare occasions it helps for comparing against a like photo shot to capture an environment.

[Related references](INDEX.md).
