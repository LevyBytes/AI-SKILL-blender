# bpy.types.ShaderNodeAttribute: properties

## ShaderNodeAttribute(ShaderNode)

### ShaderNodeAttribute(ShaderNode)

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeAttribute ( ShaderNode )

Read out attributes that are stored on objects or geometry
attribute_name

(default “”, never None)

Type :

str
attribute_type

The broad category the attribute belongs to (default 'GEOMETRY' )

- GEOMETRY
Geometry – Tied to the object's geometry, so its value can differ per vertex or throughout the object volume.

- OBJECT
Object – Tied to the object or mesh data-block itself, so it holds one uniform value.

- INSTANCER
Instancer – Tied to the instancing particle system or object, dropping back to Object mode when the attribute is absent or the object is not instanced.

- `VIEW_LAYER`
View Layer – Tied to the View Layer, Scene, or World being rendered.

Type :

Literal[‘GEOMETRY’, ‘OBJECT’, ‘INSTANCER’, ‘`VIEW_LAYER`’]

[Related references](INDEX.md).
