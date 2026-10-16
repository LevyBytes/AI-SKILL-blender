# freestyle.utils: freestyle.utils. stroke_normal ( stroke )

freestyle.utils. stroke_normal ( stroke ) 

Works out the 2D normal at the stroke vertex the iterator 'it' points to. Note that Normal2DF0D instead derives normals from the underlying FEdges, which is a poor fit for strokes once stroke geometry modifiers have already changed them.

The normals returned are dynamic, refreshing whenever the vertex position (and thus the vertex normal) shifts. When using this in geometry modifiers, you are advised to cast this generator function into a tuple or list

[Related references](INDEX.md).
