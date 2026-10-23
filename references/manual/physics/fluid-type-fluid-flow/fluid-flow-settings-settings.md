# Flow: Settings - Settings

### Settings 

Reference

Panel :

Physics ‣ Fluid ‣ Settings

Type :

Flow

Flow Type

Smoke :

Produces smoke only.

Fire + Smoke :

Produces both fire and smoke.

Fire :

Produces fire only.
The domain automatically generates accompanying smoke to represent residual combustion byproducts.

Liquid :

Produces liquid.

Flow Behavior

Dictates whether the Flow object contributes ( Inflow ), extracts ( Outflow ), or transforms the mesh into fluid material ( Geometry ).

Inflow :

This object discharges fluid into the simulation, functioning like a water source or fire base.

Outflow :

Fluid that crosses into this object's bounding box gets removed from the domain (comparable to a drain or absorption point). Useful alongside inflow objects to prevent domain saturation. Outflow objects respond to animation, with removal zones tracking their position.

Geometry :

Interior portions of this object within the domain boundary convert to simulation fluid. Multiple fluid objects may coexist. Ensure surface normals face outward or simulation accuracy suffers. Unlike domain objects, fluid objects use their actual mesh topology.

Use Flow Inflow Outflow
Enables or disables fluid transfer. This toggle assists animations where fluid addition or removal needs selective activation.

Sampling Substeps

Counts how many sub-steps diminish gaps in fluid emission from rapidly moving sources.

| Description | Description |
| --- | --- |
| Sampling sub-steps: 0.  | Sampling sub-steps: 3.  |

Note

Sub-Steps happen at each simulation step rather than per frame. The adaptive time stepping system regulates simulation step frequency.

Smoke Color

Sets the hue of discharged smoke. When different colors combine, they blend into a unified tint.

Absolute Density

When activated, the emitter generates smoke or fire exclusively when capacity exists within the emitter zone. Otherwise, continuous generation accumulates emissions.

Initial Temperature

Represents the temperature gap between emitted smoke and the domain's baseline temperature. This setting's influence on smoke depends on the domain's Heat Buoyancy configuration.

Density

Specifies the smoke quantity emitted per cycle. Higher values increase output density.

Fuel

Sets the fuel combustion rate per second. Larger values produce bigger flames; smaller values create smaller flames.

| Description | Description |
| --- | --- |
| Fuel: 0.5.  | Fuel: 1.0.  |

Vertex Group

When assigned, the designated Vertex Group constrains smoke emission zones.

[Related references](INDEX.md).
