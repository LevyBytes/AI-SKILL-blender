# bpy.types.FreestyleLineSet: edge_type_combination, edge_type_negation

edge_type_combination 

Sets how the per-edge-type selection tests are combined logically (default 'OR' )

- OR
Logical OR – Select feature edges satisfying at least one of edge type conditions.

- AND
Logical AND – Select feature edges satisfying all edge type conditions.

Type :

Literal[‘OR’, ‘AND’]
edge_type_negation 

Choose whether the edge-type tests keep matching edges or reject them (default 'INCLUSIVE' )

- INCLUSIVE
Inclusive – Select feature edges satisfying the given edge type conditions.

- EXCLUSIVE
Exclusive – Select feature edges not satisfying the given edge type conditions.

Type :

Literal[‘INCLUSIVE’, ‘EXCLUSIVE’]

[Related references](INDEX.md).
