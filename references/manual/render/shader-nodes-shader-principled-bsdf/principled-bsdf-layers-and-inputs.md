# Principled BSDF: Layers, Inputs, Diffuse, Subsurface, Specular, Transmission, Coat, Sheen, Emission

## Principled BSDF

### Principled BSDF

A unified node combining multiple layers for versatile material modeling. Based on OpenPBR Surface, compatible with Disney and Standard Surface from other software. Substance Painter textures map directly to inputs.

### Layers

The base layer mixes metal, diffuse, subsurface, and transmission. Most use one, though smooth mixing is possible. Metal is opaque reflection-only. Diffuse is fully opaque; subsurface adds below-surface scattering. Both sit below a specular layer. Transmission includes reflection and refraction. An optional glossy coat sits atop all layers. Sheen (fuzz/dust) sits on top. Light emits from below coat/sheen layers (e.g., emissive displays with coatings).

### Inputs

- **Base Color** — Material color for diffuse, subsurface, metal, transmission.
- **Roughness** — Surface microfacet roughness for specular reflection/transmission. 0.0 = sharp; 1.0 = diffuse.
- **Metallic** — Dielectric/metallic blend. 0.0 = diffuse/transmissive base with specular layer; 1.0 = specular reflection (base color tinted, no diffuse/transmission).
- **IOR** — Index of refraction. 1.0–4.0 typical. 1.5 approximates glass.
- **Alpha** — Surface transparency. 1.0 = fully opaque. Usually linked to Image Texture Alpha output.
- **Normal** — Base layer normals.

### Diffuse

- **Roughness** *(Cycles Only)* — Surface roughness. 0.0 = Lambertian; higher = Oren-Nayar.

### Subsurface

For skin, milk, wax; light scatters below surface for soft appearance.

- **Method** — Subsurface scattering simulation method.
  - **Christensen-Burley** — Approximate physically-based volume scattering. Faster convergence but less accurate than Random Walk.
  - **Random Walk** *(Cycles Only)* — True volumetric scattering. Best for closed meshes; thin/curved objects. Overlapping faces/holes cause problems.
  - **Random Walk (Skin)** *(Cycles Only)* — Optimized for skin. Auto-adjusts radius by color texture; mixes diffuse/specular transmission with custom IOR. Retains surface detail and matches measured skin.
- **Weight** — Diffuse/subsurface blend. Usually 0 or 1.
- **Radius** — Light scattering distance below surface. Higher = softer (light bleeds through). Per-RGB for materials like skin (red scatters deeper).
- **Scale** — Radius scale (0–50 cm).
- **IOR** *(Cycles Only)* — Subsurface component IOR (may differ from global IOR for skin layers).
- **Anisotropy** *(Cycles Only)* — Volumetric scattering directionality. 0 = uniform; higher = forward-scattering. Skin ≈ 0.8.

### Specular

Controls metallic and specular-layer reflection over diffuse/subsurface.

- **Distribution** — Microfacet model.
  - **GGX** — Faster than multiscatter; less physically accurate.
  - **Multiscatter GGX** — Multiple microfacet events; more energy-conserving (prevents excessive darkening).
- **IOR Level** — IOR adjustment to increase/decrease specular intensity. 0.5 = no adjustment; 0 = no reflections; 1 = double at normal incidence. Designed for easy IOR texturing.
- **Tint** — Specular/metallic reflection color tint. Non-metallic: artistic control of normal-incidence color (grazing stays white—physically correct). Metallic: edge tint simulating complex IOR (gold, copper).
- **Anisotropic** *(Cycles Only)* — Specular anisotropy. Higher = elongated highlights along tangent; negative = perpendicular.
- **Anisotropic Rotation** *(Cycles Only)* — Anisotropy direction rotation (1.0 = full circle). Note: 90° offset vs Glossy BSDF; add 0.25 to correct.
- **Tangent** — Anisotropy tangent direction.

### Transmission

For glass and liquids; surface reflects and transmits.

- **Weight** — 0 = fully opaque; 1 = fully transmissive.

### Coat

Clearcoat, lacquer, or car paint simulation.

- **Weight** — Coat layer intensity (reflection and tinting). Usually 0 or 1 for physical accuracy; may texture for variation.
- **Roughness** — Coat layer roughness.
- **IOR** — Coat IOR. Affects reflectivity and tinting falloff.
- **Tint** — Coat color tint via absorption modeling. Saturation increases at shallow angles (light travels farther through medium per IOR).
- **Normal** — Coat layer normals (e.g., smooth coating over rough surface).

### Sheen

Small surface fibers; cloth adds soft velvet-like edge reflection. Simulates dust on any material.

- **Weight** — Sheen layer intensity.
- **Roughness** — Sheen reflection roughness.
- **Tint** — Sheen reflection color.

### Emission

Surface light emission.

- **Color** — Emission color.
- **Strength** — Emission intensity. 1.0 makes object display exact Emission Color (shadeless).

[Related references](INDEX.md).
