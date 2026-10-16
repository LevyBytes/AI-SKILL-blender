# bpy.ops.wm.previews_clear

bpy.ops.wm. previews_clear ( * , id_type = set() ) 

Removes data-block previews (applicable to certain types like objects, materials, textures, etc.)

Parameters :

id_type ( set [ Literal [ 'ALL' , 'GEOMETRY' , 'SHADING' , 'SCENE' , 'COLLECTION' , 'OBJECT' , 'MATERIAL' , 'LIGHT' , 'WORLD' , 'TEXTURE' , 'IMAGE' ] ] ) – Data-Block Type, Specifies which previews to remove (optional)

- ALL
All Types.

- GEOMETRY
All Geometry Types – Clear previews for scenes, collections and objects.

- SHADING
All Shading Types – Clear previews for materials, lights, worlds, textures and images.

- SCENE
Scenes.

- COLLECTION
Collections.

- OBJECT
Objects.

- MATERIAL
Materials.

- LIGHT
Lights.

- WORLD
Worlds.

- TEXTURE
Textures.

- IMAGE
Images.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
