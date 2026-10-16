# Open Shading Language: Usage, Writing Shaders, Closures, BSDF

## Open Shading Language

### Open Shading Language

Open Shading Language (OSL) is a programmable shading framework built for sophisticated rendering systems. It empowers artists and developers to author shaders using C-like script syntax for advanced visual effects beyond standard interfaces.

Blender integrates OSL within Cycles to create custom surface, volume, and displacement shaders. This grants complete authority over shading logic, enabling procedural patterns, tailored illumination models, and geometric material behavior unavailable through prebuilt node systems alone.

Unlike node-based workflows, OSL shaders are written as text in Blender's integrated Text Editor or imported from external .osl or .oso files. After compilation, they appear in the Shader Editor via the Script Node.

Tip

OSL excels at generating procedural textures, custom material models, or prototyping research concepts. It also facilitates shader distribution across compatible applications using the OSL standard.

### Usage

To activate Open Shading Language in Blender:

- Enable OSL Rendering

In the Render Properties, activate Open Shading Language.

- Add a Script Node

In the Shader Editor, insert a Script Node, then configure its properties:

- Set Mode to Internal for a Blender text data-block, or

- Set Mode to External to load shader code from disk (.osl or compiled .oso ).

For internal mode, establish a text data-block in the Text Editor and enter your OSL code.

Blender auto-compiles the OSL source. An .osl file is compiled into .oso bytecode. Error messages appear in the system console.

- Use Shader Outputs

After compilation, the node's outputs mirror the output parameters in the OSL code. These connect anywhere in the material tree.

### Writing Shaders

Consult the OSL Documentation for comprehensive guidance.

A basic example:

shader simple_material(
color Diffuse_Color = color(0.6, 0.8, 0.6),
float Noise_Factor = 0.5,
output closure color BSDF = diffuse(N))
{
color material_color = Diffuse_Color * mix(1.0, noise(P * 10.0), Noise_Factor);
BSDF = material_color * diffuse(N);
}

### Closures

OSL diverges from languages like RSL or GLSL—it lacks a light loop. Scene lights are inaccessible; materials assemble from renderer-implemented closures. This limits flexibility but permits optimizer benefits and ensures all shaders can be importance-sampled.

Cycles closures correspond to shader nodes and their connections; consult the shader nodes documentation for specifics on behavior and parameter meanings.

See also

OSL built-in closures documentation.

### BSDF

- diffuse(N)
- oren_nayar(N, roughness)
- diffuse_ramp(N, colors[8])
- phong_ramp(N, exponent, colors[8])
- diffuse_toon(N, size, smooth)
- glossy_toon(N, size, smooth)
- translucent(N)
- reflection(N)
- refraction(N, ior)
- transparent()
- microfacet_ggx(N, roughness)
- microfacet_ggx_aniso(N, T, ax, ay)
- microfacet_ggx_refraction(N, roughness, ior)
- microfacet_beckmann(N, roughness)
- microfacet_beckmann_aniso(N, T, ax, ay)
- microfacet_beckmann_refraction(N, roughness, ior)
- ashikhmin_shirley(N, T, ax, ay)
- ashikhmin_velvet(N, roughness)

[Related references](INDEX.md).
