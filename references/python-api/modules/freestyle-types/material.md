# freestyle.types.Material

class freestyle.types. Material 

Represents a material.
__init__ ( ) 

__init__ ( brother )
__init__ ( line , diffuse , ambient , specular , emission , shininess , priority )

Constructs a FrsMaterial with the default constructor, the copy constructor, or an overloaded constructor.

Parameters :

- brother (Material) – A Material object to be used as a copy constructor.

- line (mathutils.Vector | tuple[float, float, float, float] | list[float]) – The line color.

- diffuse – The diffuse color.

- ambient (mathutils.Vector | tuple[float, float, float, float] | list[float]) – The ambient color.

- specular (mathutils.Vector | tuple[float, float, float, float] | list[float]) – The specular color.

- emission (mathutils.Vector | tuple[float, float, float, float] | list[float]) – The emissive color.

- shininess ( float ) – The shininess coefficient.

- priority ( int ) – The line color priority.
ambient 

The material's ambient color given as RGBA components.

Type :
diffuse 

The material's diffuse color given as RGBA components.

Type :
emission 

The material's emissive color given as RGBA components.

Type :
line 

The material's line color given as RGBA components.

Type :
priority 

The material's line color priority.

Type :

int
shininess 

The material's shininess coefficient.

Type :

float
specular 

The material's specular color given as RGBA components.

Type :

[Related references](INDEX.md).
