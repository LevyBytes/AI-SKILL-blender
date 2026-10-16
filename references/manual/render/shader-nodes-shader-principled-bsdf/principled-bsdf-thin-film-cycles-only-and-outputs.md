# Principled BSDF: Thin Film *(Cycles Only)*, Outputs

### Thin Film *(Cycles Only)*

Thin film interference; specular reflection becomes color-dependent on view angle, film thickness, and IOR of film and material. Common in oils, soaps, coatings; affects transmission too.

- **Thickness** — Film thickness nanometers. 0 = disabled. 100–1000 nm = strongest (visible light range).
- **IOR** — Film IOR (1.0–2.0 typical). 1.33 approximates water. At 1.0 or matching main IOR, effect vanishes (optically blends in).

### Outputs

- **BSDF** — Standard shader output.

Anisotropic rotation runs from 0.0 to 1.0.
Tangent — controls the tangent direction for anisotropy.

Transmission — used to render materials like glass and liquids, where the surface both reflects light and transmits it into the object's interior.
Weight — mix between a fully opaque surface at zero and fully transmissive at one.

Coat — a coat on top of the material, to simulate for example a clearcoat, lacquer, or car paint.
Weight — the coat layer's intensity, both reflection and tinting; typically zero or one for physically-based materials, but it can be textured to vary the amount of coating across the surface.
Roughness — the roughness of the coat layer.
IOR — index of refraction (IOR) of the coat layer, affecting its reflectivity as well as the falloff of coat tinting (from 1.0 to 2.0).
Tint — adds a colored tint to the coat layer by modeling absorption in the layer; saturation increases at shallower angles, as the light travels farther through the medium, depending on the IOR (from white to blue).
Normal — controls the normals of the Coat layer, for example to add a smooth coating on a rough surface.

Sheen — simulates very small fibers on the surface; for cloth this adds a soft velvet-like reflection near edges, and it can also simulate dust on arbitrary materials.
Weight — the intensity of the sheen layer.
Roughness — the roughness of the sheen reflection.
Tint — the color of the sheen reflection (from white to green).

Emission — light emission from the surface.
Color — the color of light emission from the surface.
Strength — the strength of the emitted light; a value of 1.0 makes the object in the image the exact same color as the Emission Color, i.e. "shadeless" (from 0.0 to 10.0).

Thin Film (Cycles Only) — simulates the effect of interference in a thin film sitting on top of the material, coloring the specular reflection in a way that strongly depends on the view angle as well as the film thickness and the index of refraction (IOR) of both the film and the material; commonly seen on e.g. oil films, soap bubbles, or glass coatings, and while its influence is most obvious in specular highlights, it also affects transmission.
Thickness — the film thickness in nanometers; a value of 0 disables the simulation, and the interference effect is strongest roughly between 100 and 1000 nanometers, near the wavelengths of visible light (illustrated from 400 to 800 nanometers).
IOR — index of refraction (IOR) of the thin film; the common range is between 1.0 (vacuum and air) and roughly 2.0, though some materials reach higher, and the default 1.33 is a good approximation for water — note that setting it to 1.0 or to the material's main IOR makes the thin-film effect disappear, since the film optically blends into the air or the material (illustrated from 1.0 to 1.5).

Outputs:
BSDF — standard shader output.

[Related references](INDEX.md).
