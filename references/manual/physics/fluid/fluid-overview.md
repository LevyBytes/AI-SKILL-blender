# Introduction

### Introduction

### Liquid Simulations

Fluid simulation represents liquid physics, mainly water. Objects in a Blender scene can enter fluid simulations. Liquid sim requires a domain setting simulation volume bounds and global parameters (viscosity, gravity).

Example of a liquid simulation. 

### Gas Simulations

Gas/smoke simulation is fluid-system subset modeling airborne solids, liquid droplets, and vapors comprising smoke. It calculates fluid airflow and generates time-varying Voxel textures capturing density, heat, and velocity for particle/fluid visualization during rendering.

Example of a fire simulation. 

Gas/smoke emits in a Domain from meshes or particle systems. Airflow responds to Effector objects and scene gravity/fields. Airflow can influence other physics via Fluid Flow force fields.

### Workflow

Liquid and gas require a Domain and at minimum one Flow object.

- Establish a Domain encompassing the simulation volume.

- Form Flow objects releasing fluid.

- Compose Effector objects for fluid interaction.

- Attach material to the domain.

- Save the .blend file.

- Bake Cache for simulation.

Note

Quick Liquid and Quick Smoke auto-create a domain with foundational liquid or smoke-and-fire material.

[Related references](INDEX.md).
