# Collisions: Troubleshooting

### Troubleshooting

Collision detection issues have several solutions:

- Speed up: raise Object/Self Collision Distance. Fastest but less accurate, cloth appears buoyant.

- Refine: increase Cloth panel Quality. Creates finer solver steps, catching fast-moving contacts better. Boost Collisions Quality for additional refinement iterations.

- Manual edit: fix the cached/baked outcome in Edit Mode if needed.

- Strengthen: raise stiffness if deforming meshes tear the cloth.

[Related references](INDEX.md).
