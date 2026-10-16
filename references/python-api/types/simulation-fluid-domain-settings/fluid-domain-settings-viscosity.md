# bpy.types.FluidDomainSettings: viscosity_base, viscosity_exponent, viscosity_value

viscosity_base

Viscosity setting: value that is multiplied by 10 to the power of (exponent*-1) (in [0, 10], default 1.0)

Type :

float
viscosity_exponent

Negative exponent for the viscosity value (to simplify entering small values e.g. 5*10^-6) (in [0, 10], default 6)

Type :

int
viscosity_value

Liquid viscosity; larger values give thicker fluids, and even 0 leaves a trace of viscosity (in [0, 10], default 0.05)

Type :

float

[Related references](INDEX.md).
