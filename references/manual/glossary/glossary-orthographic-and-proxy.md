# Glossary: Orthographic, Proxy

Orthographic
An orthographic projection keeps a viewing direction but drops the viewing point O. Now the line through P runs parallel to the viewing direction, and its crossing point S on the plane gives the orthographic projection of P. Repeat for all points P to get the orthographic view.

Proxy
In video editing a proxy is a shrunk-down stand-in for the source file, typically lower in resolution and built on an efficient codec so it loads quickly, substituting for the real image or video.

With proxies in place, editing chores like scrubbing, scrolling, and compositing speed up considerably, at the price of coarser resolution and slightly less precise results.

Quad
Quadrilateral
Quadrangle
A Face built from exactly four Vertices.

Quaternion
Quaternion Rotation
A rotation scheme described by four numbers (X, Y, Z, and W). The trio X, Y, and Z fixes an Axis while W carries an angle, yet the whole thing behaves quite unlike Axis Angle.

Geometrically, a quaternion marks a point on a unit sphere sitting in 4D space. Travel along any great circle of that sphere and you are rotating about a fixed axis, where a single loop equals two complete turns.

Radiosity
A global-illumination approach that works out how light and shadow fall when rendering images from 3D models. It is one of several Blender techniques capable of mimicking diffuse lighting.

See also
Radiosity (computer graphics)
on Wikipedia.

Random Seed
Seed
The number generators Blender relies on are pseudo-random: their output looks random, but feed them the same starting state and they replay the identical sequence every single time.

That repeatability matters for stable, reproducible results; without it a hair simulation, for instance, would shift on every re-run with no way to pin it down.

A seed encodes that starting state of the generator. Swap in a different seed and a fresh pseudo-random sequence comes out.

See also Random seed on Wikipedia.

Ray Tracing
A rendering approach that follows each light ray as it travels the scene, computing reflection, refraction, or absorption at every object the ray strikes. It beats Scanline on accuracy but pays for it heavily in speed.

Real User
A genuine Blender object that counts as a Data User, the counterpart to a Fake User, which exists only as a software bookkeeping trick.

Refraction
A wave bending its course because its speed changes. This occurs as a wave crosses from one medium, with its own Index of Refraction, into another. At the dividing line the wave shifts direction and its wavelength grows or shrinks, though its frequency holds steady.

Render
Turning 3D geometry into a finished 2D image by computation.

Resource
Outside files, images, sounds, fonts, and volume data, that you can bundle inside a blend-file.

Rest Pose
The starting transforms of one bone or an entire Armature, sometimes called the default pose. You set it in Armature Edit Mode through each bone's head, tail, and roll. Nothing added by a constraint or driver counts toward it.

RGB
A color model rooted in the classic primaries Red, Green, and Blue. Most computer displays receive RGB color straight.

Rig
The network of relationships governing how an object moves, plus the work of constructing that network.

Roll
Roll Angle
How a Bone's local X and Z axes are oriented. The local Y axis is unaffected, since the Head and Tail positions already fix it.

Rolling Shutter
On real CMOS sensors the readout happens scanline by scanline, so each scanline captures its image at a slightly different instant. That is why a horizontal camera pan can warp straight vertical lines into curves. See also Rolling Shutter on Wikipedia.

Roughness Map
A grayscale image that tells the renderer how rough or smooth a material's surface should appear. It also goes by Glossy Map.

Saturation
Saturation, or colorfulness, measures how much hue a color holds, running from desaturated grays up to vivid, intense colors.

Scanline
A rendering method that easily outpaces Ray Tracing, at the cost of a narrower effect set: reflections, refractions, motion blur, and focal blur are among those it handles less of.

Scene Referenced
An image whose Luminance channel has no imposed ceiling.

See also Display Referenced.

Shading
Reworking the color of a surface in the 3D scene according to its angle toward lights and its distance from them, producing a photorealistic look.

[Related references](INDEX.md).
