# Light Settings (Cycles): Light, Beam Shape, Settings, Nodes, Emission Shader

## Light Settings (Cycles)

### Light Settings (Cycles) 

Reference

Panel :

Properties ‣ Object Data
and Shader Editor ‣ Sidebar ‣ Options

On top of the lighting thrown by the background and by any emission-shaded object, lights give you a further way to pour illumination into a scene.
The distinction is that they never show up directly in the rendered image, and being their own object type, they are tidier to handle.

### Light 

Settings that apply no matter which renderer is active.

### Beam Shape 

Spread Area Lights
The fan width of the emitted light, ruling how diffuse the area light reads.
Wider values bring soft shadows, narrower ones a crisper light like a gridded softbox.

Example of Spread at different angles. 

### Settings 

Max Bounces
The ceiling on how many times this light's rays may Bounce.
The scene-wide bounce settings cap it.

Cast Shadow
Switch this off and intervening objects stop blocking the light.
Skipping the rays traced to the light source can speed rendering up.

Multiple Importance Sample
Out of the box lights lean on direct light sampling alone. For area lights and sharp glossy reflections that can read noisy, so flipping this on folds in indirect light sampling to quiet the noise.

Shadow Caustics
Tags a light as a refractive caustic caster. Paired with the
Cast and Receive caustics object settings,
it lets you single out objects and quicken their refractive caustic rendering.

Portals Area Lights
Area lights can pull double duty as light portals, helping sample the environment light and cutting noise hard in interior scenes.
Portals usually render slower, yet they converge sooner, so they ask for fewer samples.

Flip on the Portal option, then set area lights into windows, door openings, and anywhere light spills into the interior.

Outdoors most rays barely bounce and just sail off into the sky, so light portals buy you nothing on outdoor scenes.

White Room model by Jay Hardy. 

### Nodes 

In Cycles, shader nodes can spell out a light in full.
That unlocks rich, physically based light behavior reaching well past the basic light settings.

Note

The basic Light settings ride on top of the light output node.

You edit light shader nodes in the Shader Editor once the editor is on Light context with a light object selected.

### Emission Shader 

To set what they put out, light objects run on an Emission shader.

What the Emission shader governs:

- Color : the emitted light's spectral hue.

- Strength : how intense that emitted light is.

The Emission shader's output has to run into the
Light Output node.

[Related references](INDEX.md).
