# Camera

## Camera

This panel holds all settings of the camera used to film the movie currently edited in the Clip editor. Predefined settings can be chosen from the panel header, but settings such as distortion coefficients and the principal point aren't part of the presets and should be filled in even when a preset is used.
Sensor Width: the width of the camera's CCD sensor, found in the camera specifications.
Pixel Aspect: the CCD sensor's pixel aspect, found in the specifications or sometimes guessable: for example, if the footage should be 1920×1080 but the images themselves are 1280×1080, the pixel aspect is 1920 / 1280 = 1.5.

Lens:
Focal Length: the focal length the movie was shot with; it can be set in millimeters or pixels.
Optical Center: defines the lens's optical center (also known as the principal point); in most cases this coincides with the image center, but certain lenses have an offset optical center (refer to the camera or lens specifications if needed), and the values are given in normalized image coordinates.
Lens Distortion: the mathematical function that converts distorted to undistorted coordinates.
- Polynomial: polynomial radial distortion, using three distortion coefficients: K1, K2, and K3.
- Division: defines high distortions, making this model much better suited to cameras with fisheye lenses; uses two distortion coefficients: K1, K2.
- Nuke: the distortion model used by the Nuke compositor; uses two distortion coefficients K1, K2.
- Brown: Brown-Conrady, one of the most advanced lens-distortion models, used to model both radial and tangential distortion; can use up to four radial distortion coefficients K1 - K4 and up to two tangential distortion coefficients P1 and P2.
Coefficients — used to compensate for the lens distortion present when the movie was shot. Currently these values can only be tweaked by hand (there are no calibration tools yet) using the tools available in Distortion mode — tweak K1 until the solve is closest to the known focal length, while also taking the grid and annotations into account to prevent "impossible" distortion.
Radial Distortion Coefficients (K1 - K4): these coefficients work independently of each other; positive values give a barrel distortion while negative values give a pincushion distortion, and mixing negative and positive coefficients lets you define more complicated mustache distortions or other complex distortions that are less common but not rare.
Tangential Distortion Coefficients (P1, P2): these work independently and let you compensate for situations where the sensor isn't perpendicular to a group of lenses, which shifts (distorts) the optical center (principal point) off the sensor center: P1 compensates for sensor rotation about the Z (vertical) axis, while P2 compensates for rotation about the X (horizontal) axis; such distortions appear in footage from cameras with a sensor-stabilization system.

[Related references](INDEX.md).
