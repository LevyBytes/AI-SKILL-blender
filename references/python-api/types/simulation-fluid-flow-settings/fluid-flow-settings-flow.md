# bpy.types.FluidFlowSettings: flow_behavior, flow_source, flow_type

flow_behavior

Switch how the flow acts within the simulation (default 'GEOMETRY' )

- INFLOW
Inflow – Add fluid to simulation.

- OUTFLOW
Outflow – Delete fluid from simulation.

- GEOMETRY
Geometry – Only use given geometry for fluid.

Type :

Literal[‘INFLOW’, ‘OUTFLOW’, ‘GEOMETRY’]
flow_source

Switch the way fluid is emitted (default 'NONE' )

Type :

Literal[‘NONE’]
flow_type

Switch which kind of fluid is added in the simulation (default 'SMOKE' )

- SMOKE
Smoke – Add smoke.

- BOTH
Fire + Smoke – Add fire and smoke.

- FIRE
Fire – Add fire.

- LIQUID
Liquid – Add liquid.

Type :

Literal[‘SMOKE’, ‘BOTH’, ‘FIRE’, ‘LIQUID’]

[Related references](INDEX.md).
