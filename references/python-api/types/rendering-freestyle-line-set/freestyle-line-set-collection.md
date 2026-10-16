# bpy.types.FreestyleLineSet: collection, collection_negation

collection 

The object group that determines which feature edges become eligible for selection

Type :

Collection
collection_negation 

Choose whether feature edges tied to the object collection are kept or filtered out (default 'INCLUSIVE' )

- INCLUSIVE
Inclusive – Select feature edges belonging to some object in the group.

- EXCLUSIVE
Exclusive – Select feature edges not belonging to any object in the group.

Type :

Literal[‘INCLUSIVE’, ‘EXCLUSIVE’]

[Related references](INDEX.md).
