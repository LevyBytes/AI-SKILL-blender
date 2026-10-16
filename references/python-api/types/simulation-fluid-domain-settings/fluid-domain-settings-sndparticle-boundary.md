# bpy.types.FluidDomainSettings: sndparticle_boundary

sndparticle_boundary

What happens to particles once they exit the domain (default 'DELETE' )

- DELETE
Delete – Delete secondary particles that are inside obstacles or left the domain.

- PUSHOUT
Push Out – Push secondary particles that left the domain back into the domain.

Type :

Literal[‘DELETE’, ‘PUSHOUT’]

[Related references](INDEX.md).
