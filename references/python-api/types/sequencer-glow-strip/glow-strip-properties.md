# bpy.types.GlowStrip: properties

## GlowStrip(EffectStrip)

### GlowStrip(EffectStrip)

base classes — bpy_struct, Strip, EffectStrip
class bpy.types. GlowStrip ( EffectStrip )

A sequencer strip that produces a glow effect.
blur_radius

How far the glow spreads (in [0.5, 20], default 0.0)

Type :

float
boost_factor

Factor that scales brightness (in [0, 10], default 0.0)

Type :

float
clamp

Ceiling placed on the intensity (in [0, 1], default 0.0)

Type :

float
input_1

The effect strip’s first input (never None)

Type :

Strip
input_count

(in [0, inf], default 0, readonly)

Type :

int
quality

How precise the blur is (in [1, 5], default 0)

Type :

int
threshold

Lowest intensity that sets off a glow (in [0, 1], default 0.0)

Type :

float
use_only_boost

Display nothing but the glow buffer (default False)

Type :

bool

[Related references](INDEX.md).
