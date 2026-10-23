# Attribute Node

## Attribute Node

### Attribute Node

Retrieve attributes from an object or mesh using this node.

### Inputs

None.

### Properties

**Attribute Type**: Choose what kind of attribute data to access.

**Geometry:** The attribute comes from the object's mesh and can vary per-vertex or throughout the volume. Most geometry attributes are available through dedicated input nodes, except:

- **Ocean Foam**: Retrieves scalar values for foam regions when using an Ocean Modifier (name-dependent).

See Stack Exchange for a complete list of available options.

**Object:** Reference custom properties or RNA paths (same as driver variables). Values are defined per-object. The lookup searches the object data-block first, then the mesh data-block if not found. Custom properties take precedence over built-in ones. Properties must be integer, float, boolean, or a vector of 1–4 numeric values; invalid types return 0 on all sockets including Alpha.

Tip: The color attribute reflects the Color field in the object's Viewport Display panel, unless overridden by a custom property.

**Instancer:** Searches the instancer particle system settings, then Geometry Node instance attributes (innermost to outermost), then the instancer object. Falls back to Object mode if the current object is not instanced or the property is missing.

Warning: Currently limited to 4 layers of Geometry Node instancing.

**View Layer:** Searches the current View Layer, Scene, and World using the same lookup logic as Object, returning all zeros (including Alpha) if not found. Attributes here are uniform across the entire Render Layer.

Tip: Access useful built-in properties like: color (or world.color) for World viewport display color, render.resolution_x/y for render dimensions, camera.data.angle_x/y for active camera field of view. See driver Context Properties for an alternative lookup approach.

**Name**: Specify the attribute to retrieve.

### Outputs

- **Color**: RGB value interpolated from the attribute.
- **Vector**: XYZ value interpolated from the attribute.
- **Factor**: Scalar interpolated from the attribute.
- **Alpha**: Alpha channel when available; defaults to 1 if absent.

Warning: Currently only View Layer attributes work in shaders for World or Light Objects.

[Related references](INDEX.md).
