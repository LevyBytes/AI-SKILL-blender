# Diffusion

## Diffusion

### Diffusion

Reference

Type :

Domain

Panel :

Physics ‣ Fluid ‣ Diffusion

Liquid diffusion parameters define physical qualities and environment interaction. Viscosity and Surface Tension are primary factors. Adjusting generates virtual liquids mimicking water, oil, honey, etc. Presets for various substances exist and can be altered in the menu. Diffusion toggles in the panel header.

Viscosity

Viscosity denotes fluid "thickness": resistance to motion relative to surface area and speed.

Real-world values (dynamic viscosity) are Pascal-seconds (Pa·s) or Poise units (P = 0.1 Pa·s), often centiPoise (cP = 0.001 Pa·s).

Blender employs kinematic viscosity: dynamic viscosity ÷ density, \\(m^{2}/s\\). Example: water at room temp ≈ 1.002 cP or 0.001002 Pa·s; water density ≈ 1000 kg/m³, yielding kinematic ≈ 0.000001002 m²/s (input: 1.002×10⁻⁶).

Examples of fluids with viscosities:

| Fluid | Dynamic viscosity (in cP) | Kinematic viscosity (Blender, in \\(m^{2}/s\\) ) |
| --- | --- | --- |
| Water (20 °C) | 1.002×10 0 (1.002) | 1.002×10 -6 (0.000001002) |
| Oil SAE 50 | 5.0×10 2 (500) | 5.0×10 -5 (0.00005) |
| Honey (20 °C) | 1.0×10 4 (10,000) | 2.0×10 -3 (0.002) |
| Chocolate Syrup | 3.0×10 4 (30,000) | 3.0×10 -3 (0.003) |
| Ketchup | 1.0×10 5 (100,000) | 1.0×10 -1 (0.1) |
| Melting Glass | 1.0×10 15 | 1.0×10 0 (1.0) |

Tip

Find kinematic viscosity in correct units via Wolfram Alpha, e.g., "kinematic viscosity of alcohol in m^2/s".

Scientific notation simplifies entry: input base and 10's exponent.

Base
Viscosity base (e.g., 1.002 for water (20 °C)).

Exponent
Viscosity 10⁻¹ exponent (e.g., 6 for water).

Note

Viscosity Varies

Blender defaults appear typical and "look right" when animated. Real viscosity—especially sugar-laden (syrup, honey)—hinges on temp and concentration. Oil viscosity shifts with SAE. Room-temp glass is solid; 1500 °C glass flows like water.

Warning

The simulator doesn't fit non-flowing materials. Huge viscosity values won't behave rigidly but may cause instability.

Surface Tension
Surface tension in grid units. Higher = greater tension.

### High Viscosity Solver

High-viscosity solver targets thick liquids (honey, molasses), boosting accuracy for sluggish, dense sims.

Tip

Strength 0 applies some viscosity. Uncheck to fully disable.

Strength
Liquid viscosity. Higher = thicker.

| Description | Description |
| --- | --- |
| Strength of 0.2 (at frame 65).  | Strength of 0.4 (at frame 200).  |

[Related references](INDEX.md).
