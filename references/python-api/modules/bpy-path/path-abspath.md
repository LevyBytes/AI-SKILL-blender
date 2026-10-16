# bpy.path: bpy.path. abspath ( path , * , start = None , library = None )

bpy.path. abspath ( path , * , start = None , library = None ) 

Delivers the complete route matching the present mix file
utilizing the "//" tag.

Parameters :

- path ( str | bytes ) – The route to transform to complete.

- start ( str | bytes | None ) – Matching to this route,
when unset the present title is utilized.

- library (bpy.types.Library | None) – The archive this route is from. This is merely contained for
benefit, when the archive is not None its route swaps start .

Returns :

The complete route.

Return type :

str

[Related references](INDEX.md).
