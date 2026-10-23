# bpy.ops.preferences.extension_repo_add

bpy.ops.preferences. extension_repo_add ( * , name = '' , remote_url = '' , use_access_token = False , access_token = '' , use_sync_on_startup = False , use_custom_directory = False , custom_directory = '' , type = 'REMOTE' ) 

Enlist a fresh repository for storing extensions

Parameters :

- name ( str ) – Name, Unique repository name (optional, never None)

- remote_url ( str ) – URL, Remote URL to the extension repository, the file-system may be referenced using the file URI scheme: "file://" (optional, never None)

- use_access_token ( bool ) – Requires Access Token, Repository requires an access token (optional)

- access_token ( str ) – Secret, Personal access token, may be required by some repositories (optional, never None)

- use_sync_on_startup ( bool ) – Check for Updates on Startup, Allow Blender to check for updates upon launch (optional)

- use_custom_directory ( bool ) – Custom Directory, Manually set the path for extensions to be stored. When disabled a user's extensions directory is created. (optional)

- custom_directory ( str ) – Custom Directory, The local directory containing extensions (optional, never None)

- type ( Literal [ 'REMOTE' , 'LOCAL' ] ) – Type, The kind of repository to add (optional)

- REMOTE
Add Remote Repository – Add a repository referencing a remote repository with support for listing and updating extensions.

- LOCAL
Add Local Repository – Add a repository managed manually without referencing an external repository.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.preferences. extension_repo_add ( * , name = '' , remote_url = '' , use_access_token = False , access_token = '' , use_sync_on_startup = False , use_custom_directory = False , custom_directory = '' , type = 'REMOTE' )
Adds a new repository used to store extensions.
Parameters:
- name ( str ) – Name, Unique repository name (optional, never None)
- remote_url ( str ) – URL, Remote URL to the extension repository, the file-system may be referenced using the file URI scheme: "file://" (optional, never None)
- use_access_token ( bool ) – Requires Access Token, Repository requires an access token (optional)
- access_token ( str ) – Secret, Personal access token, may be required by some repositories (optional, never None)
- use_sync_on_startup ( bool ) – Check for Updates on Startup, Allow Blender to check for updates upon launch (optional)
- use_custom_directory ( bool ) – Custom Directory, Manually set the path for extensions to be stored. When disabled a user's extensions directory is created. (optional)
- custom_directory ( str ) – Custom Directory, The local directory containing extensions (optional, never None)
- type ( Literal [ 'REMOTE' , 'LOCAL' ] ) – Type, The kind of repository to add (optional)
- REMOTE - Add Remote Repository: add a repository referencing a remote one, with support for listing and updating extensions.
- LOCAL - Add Local Repository: add a repository managed manually, without referencing an external one.
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
