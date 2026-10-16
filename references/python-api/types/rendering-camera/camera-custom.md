# bpy.types.Camera: custom_bytecode, custom_bytecode_hash, custom_filepath, custom_mode, custom_shader

custom_bytecode

Compiled bytecode of the custom shader (default "", never None)

Type :

str
custom_bytecode_hash

Bytecode checksum for fast comparison (default "", never None)

Type :

str
custom_filepath

Shader file path for custom camera (default "", never None)

Type :

str
custom_mode

(default 'INTERNAL' )

- INTERNAL
Internal – Use internal text data-block.

- EXTERNAL
External – Use external file.

Type :

Literal['INTERNAL', 'EXTERNAL']
custom_shader

Shader for the custom camera

Type :

Text

[Related references](INDEX.md).
