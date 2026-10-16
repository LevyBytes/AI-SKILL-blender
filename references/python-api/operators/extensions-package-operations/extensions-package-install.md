# bpy.ops.extensions.package_install

bpy.ops.extensions.package_install(*, repo_directory='', repo_index=-1, pkg_id='', enable_on_install=True, url='', do_legacy_replace=False)

Retrieve and set up an extension from the web

Parameters:

- repo_directory (str) – Repo Directory, (optional, never None)
- repo_index (int) – Repo Index, (in [-inf, inf], optional)
- pkg_id (str) – Package ID, (optional, never None)
- enable_on_install (bool) – Enable on Install, Activate once set up completes (optional)
- url (str) – URL, (optional, never None)
- do_legacy_replace (bool) – Do Legacy Replace, (optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

File:

addons_core/bl_pkg/bl_extension_ops.py:1502

[Related references](INDEX.md).
