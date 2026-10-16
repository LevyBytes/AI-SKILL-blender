# Noise

## Noise

### Noise

Reference

Type :

Domain

Panel :

Physics ‣ Fluid ‣ Noise

Injecting noise into gas simulation superimposes fine detail onto the base without changing fluid motion dynamics. This adds complexity to gases (fire, smoke) minus overall motion change.

See also

Fluid noise is Wavelet Turbulence for Fluid Simulation.

Noise enablement signals cache which data to load. With Noise on but no data, the domain appears empty. Toggling doesn't reset cache; switch between base and noise.

Upres Factor
Noise resolution enhancement multiplier, tied to Resolution Divisions.

Strength
Noise magnitude. Higher = turbulent vortices.

Scale
Noise size. Higher = larger vortices.

Time
Noise animation instant, affecting field evaluation. Useful seed for wavelet noise differences between otherwise identical domains.

| Animation Time: 0.1  | Animation Time: 1.0  |
| --- | --- |
| Animation Time: 2.5  | Animation Time: 10.0  |

Note

Resolution Divisions and Upres Factor differ. Various combinations yield smoke styles.

| Description | Description |
| --- | --- |
| Resolution Divisions: 200, without noise  | Resolution Divisions: 100, Noise scale: 2.  |

Low-division high-Upres sims appear smaller in scale, creating pyroclastic plumes:

Bake Noise, Free Noise
With Modular cache type.

Progress shows in status bar; Esc pauses. After baking, Free Noise deletes cache. Pause/resume supported.

[Related references](INDEX.md).
