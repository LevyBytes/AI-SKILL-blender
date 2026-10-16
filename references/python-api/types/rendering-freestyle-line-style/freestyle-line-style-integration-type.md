# bpy.types.FreestyleLineStyle: integration_type

integration_type 

Choose how a single sort key is derived from each chain (default 'MEAN' )

- MEAN
Mean – The value computed for the chain is the mean of the values obtained for chain vertices.

- MIN
Min – The value computed for the chain is the minimum of the values obtained for chain vertices.

- MAX
Max – The value computed for the chain is the maximum of the values obtained for chain vertices.

- FIRST
First – The value computed for the chain is the value obtained for the first chain vertex.

- LAST
Last – The value computed for the chain is the value obtained for the last chain vertex.

Type :

Literal[‘MEAN’, ‘MIN’, ‘MAX’, ‘FIRST’, ‘LAST’]

[Related references](INDEX.md).
