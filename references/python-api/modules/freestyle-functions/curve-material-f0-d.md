# freestyle.functions.CurveMaterialF0D

class freestyle.functions. CurveMaterialF0D 

A stand-in for the built-in MaterialF0D when building strokes, since MaterialF0D will not operate on Curves and Strokes. Where two materials meet at a boundary, line color priority decides which of the pair is selected.

Notes: it expects to iterate across CurvePoint instances
it may return None when no fedge turns up

[Related references](INDEX.md).
