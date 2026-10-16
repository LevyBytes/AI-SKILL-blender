# bpy.ops.extensions.package_install_files

bpy.ops.extensions.package_install_files(*, filter_glob='*.zip;*.py', directory='', files=None, filepath='', repo='', enable_on_install=True, target='', overwrite=True, url='')

Install extension bundles from your disk into a user-managed source

Parameters:

- filter_glob (str) – filter_glob, (optional, never None)
- directory (str) – Directory, (optional, never None)
- files (bpy_prop_collection[OperatorFileListElement]) – files, (optional)
- filepath (str) – filepath, (optional, never None)
- repo (str) – User Repository, Deposit into this user-controlled source (optional)
- enable_on_install (bool) – Enable on Install, Activate once set up finishes (optional)
- target (str) – Legacy Target Path, Destination for legacy add-on package installation (optional)
- overwrite (bool) – Legacy Overwrite, Purge current add-ons using the matching ID (optional)
- url (str) – URL, (optional, never None)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

File:

addons_core/bl_pkg/bl_extension_ops.py:1502

[Related references](INDEX.md).
