# bpy.ops.extensions.package_uninstall

bpy.ops.extensions.package_uninstall(*, repo_directory='', repo_index=-1, pkg_id='')

Switch off and purge the extension

Parameters:

- repo_directory (str) – Repo Directory, (optional, never None)
- repo_index (int) – Repo Index, (in [-inf, inf], optional)
- pkg_id (str) – Package ID, (optional, never None)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

File:

addons_core/bl_pkg/bl_extension_ops.py:1502

[Related references](INDEX.md).
