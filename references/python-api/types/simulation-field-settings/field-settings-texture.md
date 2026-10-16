# bpy.types.FieldSettings: texture, texture_mode, texture_nabla

texture

Texture that supplies the force

Type :

Texture
texture_mode

The way the texture effect is computed (RGB and Curl require an RGB texture, otherwise Gradient is substituted) (default 'RGB' )

Type :

Literal[‘CURL’, ‘GRADIENT’, ‘RGB’]
texture_nabla

Sets the derivative offset used when computing gradient and curl (in [0.0001, 1], default 0.0)

Type :

float

[Related references](INDEX.md).
