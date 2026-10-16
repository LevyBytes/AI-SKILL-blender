# bpy.types.FreestyleLineSet: face_mark_condition, face_mark_negation

face_mark_condition 

Decide how face marks on adjacent faces qualify an edge for selection (default 'ONE' )

- ONE
One Face – Select a feature edge if either of its adjacent faces is marked.

- BOTH
Both Faces – Select a feature edge if both of its adjacent faces are marked.

Type :

Literal[‘ONE’, ‘BOTH’]
face_mark_negation 

Choose whether the face-mark tests keep matching edges or reject them (default 'INCLUSIVE' )

- INCLUSIVE
Inclusive – Select feature edges satisfying the given face mark conditions.

- EXCLUSIVE
Exclusive – Select feature edges not satisfying the given face mark conditions.

Type :

Literal[‘INCLUSIVE’, ‘EXCLUSIVE’]

[Related references](INDEX.md).
