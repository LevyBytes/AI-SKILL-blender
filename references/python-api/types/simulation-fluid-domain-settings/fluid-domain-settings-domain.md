# bpy.types.FluidDomainSettings: domain_resolution, domain_type

domain_resolution

Smoke Grid Resolution (array of 3 items, in [-inf, inf], default (0, 0, 0), readonly)

Type :

bpy_prop_array[int]
domain_type

Switch the kind of domain the simulation uses (default 'GAS' )

- GAS
Gas – Create domain for gases.

- LIQUID
Liquid – Create domain for liquids.

Type :

Literal[‘GAS’, ‘LIQUID’]

[Related references](INDEX.md).
