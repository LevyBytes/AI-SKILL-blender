# Custom Camera: Parameters, An Example, Limitations

### Parameters

Shaders may define additional inputs, exposed in the Camera properties panel under Lens options.

OSL metadata controls their interface presentation:

[[ string help = "This is a parameter" ]]
Description shown in tooltips.

[[ float sensitivity = 0.25 ]]
Increment/decrement amount when dragging or clicking.

[[ int digits = 2 ]]
Display precision for numerical parameters.

[[ float min = -5, float max = 5 ]]
Parameter range limits.

[[ int slider = 1, float slidermin = -4, float slidermax = 4 ]]
Display as a slider with specified range.

[[ string widget = "boolean" ]]
Display an int property as a checkbox (0 or 1).

### An Example

A minimal perspective camera implementation:

shader perspective_camera(
float focal_length = 90.0 [[ float sensitivity = 0.2, float min = 0 ]],
output point position = 0.0,
output vector direction = 0.0,
output color throughput = 1.0) {
vector sensor_size;
getattribute("cam:sensor_size", sensor_size);

point Pcam = camera_shader_raster_position() - point(0.5);
Pcam *= sensor_size / focal_length;
direction = normalize(vector(Pcam.x, Pcam.y, 1.0));
}

Additional examples are available in Text Editor ‣ Templates ‣ Open Shading Language .

### Limitations

Important

Custom cameras are not supported with GPU rendering unless using the OptiX backend.

Certain Cycles features—particularly the Vector pass and Window texture coordinates—need inverse mappings from rays to image coordinates, a capability not yet available with custom cameras.

[Related references](INDEX.md).
