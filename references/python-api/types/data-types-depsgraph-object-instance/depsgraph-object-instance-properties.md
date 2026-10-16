# bpy.types.DepsgraphObjectInstance: properties

## DepsgraphObjectInstance(bpy_struct)

### DepsgraphObjectInstance(bpy_struct)

base class — bpy_struct
class bpy.types. DepsgraphObjectInstance ( bpy_struct )

Further detail attached to the dependency-graph object iterator (Warning: everything exposed here is the ‘evaluated’ form, not the original .blend IDs)
instance_object

The evaluated object that this iterator is instancing (readonly)

Type :
Object
is_instance

Flags whether some other object produced this one (default False, readonly)

Type :

bool
matrix_world

The world-space transform matrix that was generated (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), readonly)

Type :

mathutils.Matrix

object

The evaluated object the iterator currently references (readonly)

Type :

Object
orco

Generated coordinates expressed in the parent object’s space (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
parent

For an instance, the parent object that produced it (readonly)

Type :

Object
particle_system

The evaluated particle system this object was instanced out of (readonly)

Type :

ParticleSystem
persistent_id

Stable identifier letting motion-blur match objects between frames (array of 8 items, in [-inf, inf], default (0, 0, 0, 0, 0, 0, 0, 0), readonly)

Type :

bpy_prop_array[int]
random_id

A random id tied to this instance, usually feeding randomized shading (in [0, inf], default 0, readonly)

Type :

int
show_particles

Whether the object’s particle portion shows up in the render (default False, readonly)

Type :

bool
show_self

Whether the object’s own geometry shows up in the render (default False, readonly)

Type :

bool
uv

UV coordinates expressed in the parent object’s space (array of 2 items, in [-inf, inf], default (0.0, 0.0), readonly)

Type :

bpy_prop_array[float]

[Related references](INDEX.md).
