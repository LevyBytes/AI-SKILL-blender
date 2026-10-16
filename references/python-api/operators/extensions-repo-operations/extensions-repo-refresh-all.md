# bpy.ops.extensions.repo_refresh_all

bpy.ops.extensions.repo_refresh_all(*, use_active_only=False)

Sync extension & legacy add-ons by dumping and re-importing code & metadata (akin to reboot)

Parameters:

use_active_only (bool) – Active Only, Refresh only the chosen source (optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

File:

addons_core/bl_pkg/bl_extension_ops.py:1744

[Related references](INDEX.md).
