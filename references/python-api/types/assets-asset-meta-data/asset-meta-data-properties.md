# bpy.types.AssetMetaData: properties

## AssetMetaData(bpy_struct)

Supplementary information about an asset data block.

base class — bpy_struct
class bpy.types. AssetMetaData ( bpy_struct )

Extended metadata for asset identification and organization.
active_tag

Index of the tag set for editing (in [-32768, 32767], default 0)

Type :

int
author

Name of the creator of the asset (default "", never None)

Type :

str
catalog_id

Identifier for the asset's catalog, used by Blender to look up the asset's catalog path. Must be a UUID according to RFC4122. (default "", never None)

Type :

str
catalog_simple_name

Simple name of the asset's catalog, for debugging and data recovery purposes (default "", readonly, never None)

Type :

str
copyright

Copyright notice for this asset. An empty copyright notice does not necessarily indicate that this is copyright-free. Contact the author if any clarification is needed. (default "", never None)

Type :

str
description

A description of the asset to be displayed for the user (default "", never None)

Type :

str
license

The type of license this asset is distributed under. An empty license name does not necessarily indicate that this is free of licensing terms. Contact the author if any clarification is needed. (default "", never None)

Type :

str
tags

Custom tags (name tokens) for the asset, used for filtering and general asset management (default None, readonly)

Type :

AssetTags[AssetTag]

[Related references](INDEX.md).
