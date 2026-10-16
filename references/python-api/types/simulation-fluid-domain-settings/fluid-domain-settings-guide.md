# bpy.types.FluidDomainSettings: guide_alpha, guide_beta, guide_parent, guide_source, guide_vel_factor

guide_alpha

Guiding weight; larger values introduce more lag (in [1, 100], default 2.0)

Type :

float
guide_beta

Guiding size; larger values make bigger vortices (in [1, 50], default 5)

Type :

int
guide_parent

Borrow this object's velocities for the guiding effect (the object must carry a fluid modifier and be of the domain type) (in source: object needs to have fluid modifier and be of type domain)

Type :

Object
guide_source

Pick where guiding velocities come from (default 'DOMAIN' )

- DOMAIN
Domain – Use a fluid domain for guiding (domain needs to be baked already so that velocities can be extracted). Guiding domain can be of any type (i.e. gas or liquid)..

- EFFECTOR
Effector – Use guiding (effector) objects to create fluid guiding (guiding objects should be animated and baked once set up completely).

Type :

Literal[‘DOMAIN’, ‘EFFECTOR’]
guide_vel_factor

Guiding velocity factor; larger values yield stronger guiding velocities (in [0, 100], default 2.0)

Type :

float

[Related references](INDEX.md).
