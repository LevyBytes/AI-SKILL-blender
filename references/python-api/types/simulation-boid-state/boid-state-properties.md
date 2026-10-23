# bpy.types.BoidState: properties

## BoidState(bpy_struct)

### BoidState(bpy_struct)

base class: bpy_struct
class bpy.types.BoidState(bpy_struct)

A behavioral state used by the boid simulation
active_boid_rule

(readonly)

Type:
BoidRule
active_boid_rule_index

(in [0, inf], default 0)

Type:
int
falloff

(in [0, 10], default 0.0)

Type:
float
name

Boid state name (default "", never None)

Type:
str
rule_fuzzy

(in [0, 1], default 0.0)

Type:
float
rules

(default None, readonly)

Type:
bpy_prop_collection[BoidRule]
ruleset_type

Method by which the listed rules are processed (default 'FUZZY')

- FUZZY
Fuzzy – Rules are gone through top to bottom (only the first rule which effect is above fuzziness threshold is evaluated).

- RANDOM
Random – A random rule is selected for each boid.

- AVERAGE
Average – All rules are averaged.

Type:
Literal['FUZZY', 'RANDOM', 'AVERAGE']
volume

(in [0, 100], default 0.0)

Type:
float

[Related references](INDEX.md).
