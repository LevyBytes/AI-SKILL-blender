# Advect Grid Node

## Advect Grid Node

Moves voxel values through a velocity field over time via numerical integration. Advection evolves quantities (density, temperature, color) according to flow fields; used in fluid, smoke, motion simulation. Supports multiple integration schemes; trades speed, accuracy, stability. Works on scalar/vector grids with uniform voxel scale. Conceptually: trace each voxel backward through velocity field by time step, sample previous grid value, assign to current voxel.

Inputs:
- Grid: Grid to advect (uniform voxel scale required)
- Velocity: Vector grid defining flow direction/magnitude; determines value transport through space
- Time Step: Advection time step in seconds; larger values = faster motion; may reduce accuracy/stability

Integration Scheme:
- Semi-Lagrangian: First-order, fastest, most stable; introduces noticeable numerical diffusion (blurring)
- Midpoint: Second-order; balances speed/accuracy for most cases
- Runge-Kutta 3: Third-order; higher accuracy, moderate cost
- Runge-Kutta 4: Fourth-order, highest single-step accuracy; ideal for detailed simulations, slower
- MacCormack: Implicit diffusion control; reduces dissipation while maintaining stability
- BFECC: Back and Forth Error Compensation and Correction; minimizes dissipation, maintains sharp features

Limiter — Overshoot/undershoot strategy:
- None: No limiting; fastest; can introduce gradient-region artifacts
- Clamp: Constrains values to original neighborhood range; prevents over/undershooting, preserves stability
- Revert: Falls back to first-order where clamping necessary; more conservative/stable than clamping alone

Properties:
Data Type: Grid data type (Float, Integer, Vector). Determines field type being advected.

Outputs:
- Grid: Advected grid after Time Step elapsed; each voxel value transported by velocity field and integration scheme

[Related references](INDEX.md).
