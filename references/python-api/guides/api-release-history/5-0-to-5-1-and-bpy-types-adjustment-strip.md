# API release history: 5.0 to 5.1, bpy.types.AdjustmentStrip, Added, bpy.types.Brush, Removed, bpy.types.BrushCapabilitiesSculpt, Added, bpy.types.BrushGpencilSettings, Added, bpy.types.CompositorNode, Removed, bpy.types.CompositorNodeAlphaOver, Removed, bpy.types.CompositorNodeAntiAliasing, Removed, bpy.types.CompositorNodeBilateralblur, Removed, bpy.types.CompositorNodeBlur, Removed, bpy.types.CompositorNodeBokehBlur, Removed

## Change Log

### Change Log

What shifted in Blender's Python API from one release to the next.

### 5.0 to 5.1

### bpy.types.AdjustmentStrip

#### Added

- bpy.types.AdjustmentStrip.content_trim_end

- bpy.types.AdjustmentStrip.content_trim_start

### bpy.types.Brush

#### Removed

- use_airbrush

- use_anchor

- use_curve

- use_line

- use_restore_mesh

- use_space

### bpy.types.BrushCapabilitiesSculpt

#### Added

- bpy.types.BrushCapabilitiesSculpt.has_hardness

- bpy.types.BrushCapabilitiesSculpt.has_normal_radius

### bpy.types.BrushGpencilSettings

#### Added

- bpy.types.BrushGpencilSettings.stroke_type

### bpy.types.CompositorNode

#### Removed

- tag_need_exec

- update

### bpy.types.CompositorNodeAlphaOver

#### Removed

- update

### bpy.types.CompositorNodeAntiAliasing

#### Removed

- update

### bpy.types.CompositorNodeBilateralblur

#### Removed

- update

### bpy.types.CompositorNodeBlur

#### Removed

- update

### bpy.types.CompositorNodeBokehBlur

#### Removed

- update

[Related references](INDEX.md).
