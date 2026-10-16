# USD primvar types and accessibility

USD Primvar data types — Blender handles a portion of the USD basic data types when importing and exporting; only those its attribute system natively understands are processed.
- Boolean — bool.
- 8-Bit Integer — uchar. USD's unsigned 8-bit value is cast to signed on import, and the signed value cast to unsigned on export.
- Integer — int. A 32-bit signed integer.
- Float — float. A 32-bit, single-precision float.
- Vector — float3. A 3D vector of 32-bit floats.
- 2D Vector — float2/texCoord2f. A 2D vector of 32-bit floats.
- Color — color4f. An RGBA color of 32-bit floats; as a special case, a Primvar or attribute for USD's displayColor reads or writes as color3f with an Alpha of 1.0.
- Byte Color — color4f. USD has no byte-color equivalent, so byte values convert to float and export as color4f.
- Quaternion — quatf. A floating-point Quaternion rotation.
Implementation Caveats — Blender doesn't support USD Primvars in 64-bit integers (int64), unsigned types (uint), or 64-bit double-precision or 16-bit half-precision floats; that rules out, for example, matrix4d (a 4×4 matrix of doubles) and quath (a half-precision quaternion). Note: the USD float4 type has no direct Blender equivalent and won't be read as a Blender Color or Quaternion.

USD UI Accessibility — Blender can author and load the UsdUIAccessibilityAPI schema on every supported data-block type that allows Custom Properties; the API records accessibility information for a USD primitive that a runtime's accessibility frameworks may surface, if present. Besides the root-prim accessibility export option above, you can set per-object accessibility info like so:
- Add these String Properties to the object data-block:
- Required: `accessibility:<namespace>:label` and `accessibility:<namespace>:description`.
- Optional: `accessibility:<namespace>:priority`.
The `<namespace>` may be any valid USD primvar identifier, including default, which is the recommended convention; priority may be low, standard, or high. It's well worth filling in the accessibility fields on the root prim for any long-lived USD document that may reach a wide range of software and people — when uploading to an asset marketplace, say. Implementation Caveats: Blender doesn't support time-varying accessibility schemas, since custom String properties can't be animated.

[Related references](INDEX.md).
