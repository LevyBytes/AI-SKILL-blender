# Usage: Display Mode, Stereo 3D Camera, Convergence Mode, Viewport Stereo 3D

### Display Mode 

Anaglyph
Produces two distinctly tinted color images, each tailored to one eye. Anaglyph glasses are required. Red-cyan, green-magenta, and yellow-blue variants are available.

Interlace
Merges both eye views into a single interlaced frame. A 3D-compatible display is necessary. Row, Column, and Checkerboard interlacing modes are supported. A Swap Left/Right option adjusts for screen calibration. Best results in full-screen mode.

Time Sequential
Alternates rendering per eye. Also termed Page Flip. Quad Buffer support from the GPU is mandatory and requires full-screen operation.

Side-by-Side
Places left and right eye views side-by-side. Cross-Eye viewing option is available. Full-screen operation is necessary, best paired with the Full Editor option.

Top-Bottom
Stacks left and right eye perspectives vertically. Full-screen and Full Editor operation required.

Note

Full Screen Stereo 3D Modes

For constant stereo 3D viewing, most workflows benefit from full-screen stereo operation. Certain modes function exclusively in full-screen, concealing much of the interface. Two-monitor setups work well: reserve the 3D display for stereo visualization and use the other for standard Blender editing.

### Stereo 3D Camera 

Stereo 3D scene configuration generates a camera pair dynamically for rendering and viewport preview. This behaves like two cameras with shared parameters (focal length, clipping planes, …). The pair is offset and can exhibit independent rotation and perspective shifts.

Stereo 3D camera settings. 

Interocular Distance
The separation between stereo camera pair. Though convergence can be adjusted post-render, distinct interocular distances produce varying outcomes due to differential scene occlusion across viewpoints.

Convergence Plane Distance
The stereo camera convergence point, typically representing the distance between a projector and its screen. Real-time visualization is available in the 3D Viewport.

Spherical Stereo
Renders by rotating the camera around the interocular midpoint for each pixel.

Use Pole Merge
Taper interocular distance toward zero beyond a specific angle cutoff.

Pole Merge Start Angle
The threshold angle where tapering starts.

Pole Merge End Angle
The point angle where interocular distance becomes zero.

### Convergence Mode 

Off-Axis
The camera pair separates by interocular distance and shifts inward to meet at the convergence plane. This represents the ideal configuration, closest to human vision mechanics.

Parallel
Generates two non-converging parallel cameras. This needs post-render alignment and cannot be used directly for viewing. Typical when combining practical footage with CG elements.

Toe-in
Angles cameras rather than shifting frustums. Toe-in remains uncommon in modern visual effects work.

Pivot
The stereo pair can be generated around the main camera with separate cameras per eye (Center Pivot) or with an existing camera as base and generation of (Left or Right). The latter applies when rendering a single eye for a single-view 2D project converted from mono.

### Viewport Stereo 3D 

Activating Views in the Render Layer panel exposes a fresh control area in the 3D Viewport Sidebar. Configure whether the viewport displays stereo 3D output and which camera to show. The panel also permits visibility of individual Cameras, the Plane, and stereo frustums.

Viewport stereo 3D settings. 

Cameras
With Stereo 3D Viewport operation, examine each dynamically-built camera output or their combined result. Multi-View mode displays the merged left-and-right camera result (when both exist) or the currently-selected camera.

Plane
The convergence plane represents the audience viewing surface. Viewport visualization allows depth planning based on script requirements beyond the camera bounds.

Volume
The merged stereo camera frustums help prevent visibility mistakes by identifying where one camera sees content the other doesn't. Boundaries depend on camera clip distances. Retinal rivalry zones (visible to only one camera) are tolerated in the negative space (the region from the convergence plane into the image) but are to be avoided in the positive space (the area from the convergence plane to the camera).

Viewport 3D: convergence plane and volume display.

[Related references](INDEX.md).
