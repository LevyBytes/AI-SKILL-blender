# Usd import options

Importing USD Files: USD files usually lay out the scene as a hierarchy of primitives, or prims, each holding data for a scene entity such as geometry, lights, cameras, and transform hierarchies. Blender's USD importer turns USD prims into a hierarchy of Blender objects; like the exporter, it doesn't yet handle certain USD composition concepts, such as layers and references. These USD data types can import as Blender objects: Cameras, Curves, Lights, Materials, Meshes, Point Clouds, Primitive Shapes, and Volumes. For how each type is handled, see the Import Options below. Note: when importing a USDZ archive, weigh the Import Textures option carefully to decide whether and how to copy texture files out of the zip archive.

Xform and Scope Primitives — USD's Xform prim type holds transform data and can represent transform hierarchies and organize the scene; Xform prims import as Blender empty objects. USD also has Scope primitives — entities with no transform data that simply group other scene elements; Blender has no exact counterpart, so these import as Blender empties at the origin, an imperfect match (empties have a transform, Scopes don't) that nonetheless helps keep the scene hierarchy's structure.

PointInstancer Primitives: USD's UsdGeomPointInstancer prim type holds instances scattered over a primitive's points; these come into Blender as Point Clouds built with a Geometry Nodes Modifier and the Instance on Points Node.

Animations: the importer supports two kinds:
- Animating transforms: when a USD primitive carries time-varying transform data, a Transform Cache constraint is attached to the resulting Blender object.
- Animating geometry: animated mesh, curve, and point-cloud data is handled by attaching a Mesh Sequence Cache modifier to the imported data. Geometry attribute (USD Primvar) animation is supported for every data type with a Blender equivalent, including colors, UVs, velocities, and other generic attribute data. Note: USD file sequences (a unique file per frame) aren't supported.

Materials: when a USD mesh or geometry subset comes with a bound material, the importer hands the Blender object a material whose name matches the USD material; if a Blender material of that name already exists, it may be reused depending on the Material Name Collision option, otherwise a new one is created. When a USD material carries a USD Preview Surface shader source, its Viewport Display color, metallic, and roughness come from the matching USD Preview Surface inputs. There's also an Import USD Preview option that converts USD Preview Surface shaders to Blender Principled BSDF nodes; it can be lossy, since it doesn't yet handle every shader setting and type, but it produces approximate material visualizations.

Coordinate System Orientation: if the imported USD is Y up, a rotation is applied automatically to root objects to convert to Blender's Z up.

Import Options: these are available when importing from USD:
General:
Path Mask: imports just the part of the USD scene that hangs below the given primitive.
Include:
  Visible Primitives Only: skips invisible USD primitives; applies only to primitives with a non-animated visibility attribute, while ones with animated visibility always import.
  Defined Primitives Only: off, this allows importing USD primitives that aren't defined, such as those with an override specifier.
Set Frame Range: updates the scene's start and end frame to match the USD stage's.
Create Collection: adds all imported objects to a new collection.
Relative Path: picks the file relative to the blend-file.
Apply Unit Conversion Scale: scales the scene objects by the USD Stage metersPerUnit value, on top of the Scale option's value.
Scale: how much to scale the imported objects about the world's origin.
Light Intensity Scale: a scale for the intensity of imported lights.
Custom Properties: how to import USD attributes as Custom Properties. None (skip USD custom attributes), User (import attributes in the userProperties namespace as custom properties, with the namespace stripped from the names), or All Custom (import every USD custom attribute as a custom property, keeping namespaces in the names).
Object Types:
Cameras: imports UsdGeomCamera primitives as Camera Objects. Supported attributes include projection type (perspective and orthographic), focal length, depth-of-field distance, F-stop (aperture), clipping start and end, sensor shift (tilt) X and Y, and sensor size (aperture width and height). Note: most properties support animation, but aperture-size import is limited by differences between USD and Blender in how sensor dimensions are read; when aperture sizes are animated, the matching shift values are animated too for consistency.
Curves: imports UsdGeomBasisCurves primitives as Curves and UsdGeomNurbsCurves as Blender meshes.
Lights: imports lights as Light Objects; cylinder and geometry lights aren't included yet.
World Dome Light: turns the first UsdLuxDomeLight or UsdLuxDomeLight_1 dome light it finds into a world background shader.
Materials: imports UsdPreviewSurface materials.
Meshes: imports UsdGeomMesh primitives as Mesh Objects.
Volumes: imports UsdVolVolume OpenVDB assets as Volume Objects.
Point Clouds: imports UsdGeomPoints primitives as Point Cloud Objects.
USD Shapes: imports USD primitive shapes as Blender meshes; UsdGeomCapsule, UsdGeomCapsule_1, UsdGeomCone, UsdGeomCube, UsdGeomCylinder, UsdGeomCylinder_1, UsdGeomPlane, and UsdGeomSphere are supported.
Display Purpose:
  Render: includes primitives with purpose render.
  Proxy: includes primitives with purpose proxy.
  Guide: includes primitives with purpose guide.
Material Purpose: tries to import materials with the given purpose; if none of that purpose is bound to the primitive, the fallback behavior (if any) is noted below.

All Purpose: tries to import allPurpose materials.
Preview: tries to import preview materials, falling back to allPurpose ones.
Full: tries to import full materials, falling back to allPurpose then preview, in that order.

Geometry:
UV Coordinates: reads mesh UV coordinates.
Color Attributes: turns the USD mesh displayColor values into Blender's Color Attributes.
Mesh Attributes: reads USD Primvars as mesh attributes.
Subdivision: adds Subdivision Surface modifiers based on the USD SubdivisionScheme attribute.
Validate Meshes: checks the imported mesh for corrupt data and repairs it if needed; with it off, bad data may crash display or editing. It slows importing but is recommended, since data errors aren't always obvious.
Merge parent Xform: lets a USD primitive merge with its Xform parent when it's the parent's only child.

Rigging:
Shape Keys: imports USD blend shapes as Blender Shape Keys.
Armatures: imports USD skeletons as Blender Armatures.

Materials:
Import All Materials: also imports materials that no geometry uses; with this off, materials referenced by geometry still come in.
Import USD Preview: converts USD Preview Surface shaders to Principled BSDF shader networks.
Set Material Blend: when Import USD Preview is on, the material's blend method is set automatically from the opacity and opacityThreshold shader inputs, letting transparent objects show correctly.
Material Name Collision: what to do when an imported material's name clashes with an existing one. Make Unique (bring each material in as its own Blender material) or Reference Existing (point at the existing material of that name rather than importing).

Textures: when importing a USDZ package, these options decide whether and how the USD's texture asset dependencies are copied out of the zip archive so Blender can load them.
Import Textures: how textures from a USDZ archive are handled. None (skip them; material textures may then fail to resolve in Blender), Packed (bring textures in as packed data in the Blender file), or Copy (copy files to the Textures Directory below).
Textures Directory: where imported textures land when Import Textures is set to Copy. The default is the relative path //textures, which needs the Blender file saved first so the relative path can resolve.
File Name Collision: what to do when an imported texture filename clashes with an existing file. Use Existing (use the existing file rather than copying) or Overwrite (overwrite it).

Particles and Instancing:
Scene Instancing: imports USD scene-graph instances as collection instances; otherwise they come in as copies.

[Related references](INDEX.md).
