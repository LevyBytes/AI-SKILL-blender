# Introduction

Blender's 2D video stabilization builds on its image feature-tracking: you use tracking points to remove shake, bumps, and jerks from footage. It's typically part of a 2D workflow that prepares and improves footage before further processing or modeling. This page explains how it works, introduces the related terms and concepts, details the interface controls, and ends with practical hints. Typical uses: fixing minor flaws (a shaky tripod, a jerk in camera movement); a "poor man's steadycam" when a real one wasn't available, affordable, or practical; and prepping footage for masking, matching, and rotoscoping. 2D stabilization often has to cope with somewhat imperfect, flawed footage.

How It Works: to detect spurious movement in a shot, the stabilizer assumes a simplified movement model and fits the tracked features' movement to it to derive a compensation. This only works as far as the model is adequate, yet in practice the approach works surprisingly well even on complicated shots where the basic assumption is just an approximation of much more elaborate movement. The model assumes movement by an affine-linear transform: the camera is pushed up/down/sideways by a translation component, then the image is tilted and scaled around a pivot point (the rotation center). Compensation proceeds in two steps: first the translation offset is detected from the weighted average of all translation tracking points; after compensating it, additional rotation/scale tracking points detect rotation around a given pivot, again via a weighted average of those points. In the current version the pivot is anchored to the weight center of the translation tracking points, so the detected translation is effectively factored out — not always optimal, especially when tracks have gaps or don't span the whole footage, and better pivot control is planned for future releases.

Stabilization Tracks: any stabilization needs tracked image features to derive the movements; these tracking points or "tracks" come from Blender's image feature-tracking component. Choosing which points to track is tricky but crucial — since you're often dealing with imperfect footage, averaging tracks helps work around image or tracking errors, and when the footage has perspective-induced movement, tracking points placed symmetrically above and below the horizon can cancel spurious movement and stabilize the focal area between them. Tracks go into two groups: first, a list used to compensate for jumps in camera location, from which a weighted average is computed and kept constant through the whole shot (so it's good to use markers close to and centered on the most important subject); and second, a selection used to keep the image's rotation and scale constant, where you may reuse the same tracks but usually do best with points far from the image center and symmetric on both sides to capture angular movement more precisely, again averaged and held constant.

Footage, Image & Canvas: stabilizing video means distinguishing several frames of reference. The image elements in the footage move irregularly within the original image boundaries — the very reason we stabilize. When stabilization succeeds, those elements can be considered stable while, in exchange, the footage's image boundaries take on irregular movement and jump around the opposite way. Since the actual subject is now stable, we can treat it as attached to a fixed backdrop, which we call the canvas. The canvas concept helps handle deliberate camera moves and offers another benefit: video pixels are frequently non-square, so they must be stretched and expanded before any sensible rotation stabilization, making the canvas, by definition, the reference for an undistorted display of the image contents. When the camera was moved intentionally, there's yet another frame of reference beyond the canvas: the frame (or "cadre") of the final image we want to create. To see the distinction, consider a hand-held pan to the right: since the camera turned right, the contents move left within the original frame, but if the stabilizer succeeds in "fixing" the contents relative to the canvas, the original boundaries drift irregularly to the right and the contents gradually vanish behind the left boundary — pan far enough and you're left with an empty black backdrop. The only fix is to move the final image frame along to the right, following the originally intended pan, this time smoothly and cleanly.

Animate Expected position/rotation/scale to apply intentional camera movement.

The "Dancing" Black Borders

Stabilization success creates jittery footage boundaries (inevitable). Zoom-reduction hides them; Expected position animation centers content to lower zoom demand.

Autoscale finds minimum zoom eliminating borders. Large jumps trigger over-zoom (single zoom across entire duration). Manual animation of zoom + Expected position often yields better results.

Motion Tracking serves camera/object motion capture and applies tracking data to 3D objects (created or imported) via constraints.

Blender's toolkit includes powerful 2D tracking and 3D reconstruction (camera and object tracking), plus specialized features (plane tracks for compositing). Tracks also drive Mask Editor deformation for rotoscoping.

Views

Tracking Mode offers three views; toggle using the header selector. The entire Movie Clip editor switches. To show curve or dope sheet, split the editor with one in the alternate view.

Manual Lens Calibration

All cameras record distorted video—intrinsic to optical design.

Accurate camera solving demands exact focal length and distortion values.

Focal length comes from camera settings or EXIF; external OpenCV tools estimate distortion. Within Blender, use Annotation tool to draw (poly line brush) straight edges on footage; adjust distortion values until annotations align edges.

For precision, OpenCV Grid calibration (identical distortion model) suits Blender workflows.

Camera and Object Motion Solving

Blender solves camera motion (including tripod shots) and object motion relative to camera. Plane Tracks solve marker motion across a single plane.

Tools for Scene Orientation and Stabilization

Post-solve, orient the 3D scene for convenient compositing. Tools define floor, origin, and X/Y axes.

Footage often contains spurious jumps, jitter, or handheld camera wobble. 2D Stabilization detects and compensates such motion (based on tracked elements) to enhance final quality.

[Related references](INDEX.md).
