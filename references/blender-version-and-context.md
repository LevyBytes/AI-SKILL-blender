# Blender version and context

Match the documented Blender version, object type, mode and renderer before applying a reference. Manual controls, RNA data access and `bpy.ops` operators are distinct interfaces.

- Keep exact operator names, API identifiers, enum values, shortcuts and platform conditions.
- Action behavior changes across Blender versions; use the version stated in the contract.
- Grease Pencil modifiers and general object modifiers have different contracts.
- Preserve renderer-specific light settings and power units.
- Python threading and data-reference invalidation have specific restrictions; consult the API limitations guides.
- Coordinate spaces matter. The KDTree example converts the cursor to object-local coordinates.
- Read the complete parameter and return contract, including prerequisite example modules.
- Blender manual contribution and translation instructions describe Blender's documentation project, not this package's translation coverage.

The repair sources are pinned to Blender 5.1. Historical release notes and explicitly versioned material retain their own version conditions. These references do not establish native Blender execution results.

[Reference index](INDEX.md).
