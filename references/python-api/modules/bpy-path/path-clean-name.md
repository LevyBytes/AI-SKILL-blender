# bpy.path: bpy.path. clean_name ( name , * , replace = '_' )

bpy.path. clean_name ( name , * , replace = '_' ) 

Delivers a label with characters swapped that
might generate issues under numerous cases,
for instance composing to a document.

Every sign other than A-Z/a-z, 0-9 is swapped with "_"
or the substitute input if laid out.

Parameters :

- name ( str | bytes ) – The route designation.

- replace ( str ) – The substitute for illegitimate marks.

Returns :

The cleansed designation.

Return type :

str

[Related references](INDEX.md).
