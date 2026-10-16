# bpy.props: Property Definitions (bpy.props)

### Property Definitions (bpy.props) 

This unit establishes qualities to elongate Blender's interior material. The result of these operations is utilized to attribute qualities to groupings enlisted with Blender and cannot be utilized immediately.

Note

Every input to these operations must be transmitted as named.

### Assigning to Existing Classes 

Tailored qualities can be supplied to every subclass of an ID ,
Bone and PoseBone .

These qualities can be shifted, obtained by the client contact and Python
like Blender's pre-existing qualities.

Warning

Gain to these qualities might occur in concurrent framework, on a per-material-section basis.
This must be attentively examined when applying accessors or upgrade functions.

Customarily, these functions should not change every other information that the one managed by their material-section.
When acquiring outside non-Blender material, concurrent protection procedures must be examined.

```python
import bpy

### Assign a custom property to an existing type.
bpy.types.Material.custom_float = bpy.props.FloatProperty(name="Test Property")

### Test the property is there.
bpy.data.materials[0].custom_float = 5.0
```

### Operator Example 

A widespread application of tailored qualities is for Python based Operator
groupings. Examine this regulation by operating it in the manuscript editor, or by selecting the
switch in the 3D Display's Apparatus section. The previous will display the qualities
in the Redo portion and let you modify them.

[Related references](INDEX.md).
