# Object: Caustics, Light Group, Light Linking, Shadow Linking

### Caustics 

Tag objects as caustic casters or receivers. This pairs with a
Light or
World Shader carrying Shadow Caustics
to selectively quicken caustic rendering on objects in your scene.

Note

The speed-up for caustic rendering leans on
MNEE . Both that approach and its Cycles build come hedged with a number of limits:

- It handles refractive caustics living in object shadows and nothing more. Reflection caustics, or any caustic landing outside a shadow, simply go unrendered.

- Being an approximation, MNEE Caustics turn out physically wrong in plenty of cases, brightnesses that miss and a faulty take on caustics from rough or curved surfaces among them.

- Where a complex material packs several refractive BSDFs, only one of them gets caustics out of MNEE.

- Any Filter Glossy setting is disregarded once MNEE is doing the refractive caustics.

- An MNEE Caustic ray may cross at most 6 Caustic Caster surfaces on its way from a Caustic Receiver to a Shadow Caustic light; beyond that the ray dies and its caustics drop out.

- While the scene holds an active Caustic caster, Caustic receiver, and Shadow Caustic Light together, the Ambient Occlusion and Bevel nodes return nothing valid on any object acting as a Caustic caster or receiver.

- Smooth normals on the caustic caster are a prerequisite for MNEE Caustics to fire at all.

- The MNEE caustic calculation pays volumetric materials no attention.

- Bump and normal maps drop out of the caustic calculation as well.

Cast Shadow Caustics
Tag an object as a caustic caster.

Receive Shadow Caustics
Tag an object as a caustic receiver.

| Description | Description |
| --- | --- |
| Rendering caustics inside an eye without MNEE at 32 samples per pixel.  | Rendering caustics inside an eye using MNEE at 32 samples per pixel.  |

### Light Group 

Light Group
Pick the Light Group the current Object or Light should join.

Add Light Group
Type a name into the Light Group field that no existing Light Group bears, hit this button, and Blender spins up a Light Group under that name and drops the chosen Object or Light into it.

### Light Linking 

Through Light Linking, pen a light's reach to a named set of objects.

Receiver Collection
The collection of objects that take in light the object emits.

### Shadow Linking 

Through Light Linking, pen the shadows to a named set of objects.

Shadow Blocker Collection
The collection of objects standing as shadow blockers for light the object emits.

[Related references](INDEX.md).
