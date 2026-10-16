# freestyle.types.StrokeShader

class freestyle.types. StrokeShader 

Serves as the parent type for stroke shaders. Every stroke shader has to derive from this class and override the shade() method. A StrokeShader exists to alter stroke attributes such as thickness, color, geometry, texture, blending mode, and the like. The usual approach is to walk the Stroke's stroke vertices and adjust each one's StrokeAttribute. Below is a code example showing such a loop:

```python
it = ioStroke.strokeVerticesBegin()
while not it.is_end:
    att = it.object.attribute
    # Perform the intended attribute modification here.
    it.increment()
```
__init__ ( ) 

Default constructor.
shade ( stroke ) 

The shading method. Must be overloaded by inherited classes.

Parameters :

stroke (Stroke) – A Stroke object.
name 

The name of the stroke shader.

Type :

str

[Related references](INDEX.md).
