# Custom Camera: Using Custom Cameras, Writing Camera Shaders, Inputs, Outputs, Attributes, Derivatives

## Custom Camera

### Custom Camera

Cycles goes beyond standard camera models (Perspective, Orthographic, and Panoramic) to support user-defined cameras implemented in Open Shading Language (OSL). Custom cameras function as OSL shaders receiving a sensor position as input and outputting the ray's origin, direction, and throughput.

OSL for shading and custom cameras operate independently; custom cameras work even when OSL shading remains disabled.

### Using Custom Cameras

To employ a custom camera, set the lens type to Custom.

This activates selection of a text data-block or external file, mirroring the Script node in shaders.

If the chosen camera shader contains parameters, they display below the Lens panel.

### Writing Camera Shaders

### Inputs

The camera shader's primary input is the sensor position, provided by camera_shader_raster_position() , which returns a point with X and Y values representing image position in the 0-1 range.

To allow random variation in shader sampling, camera_shader_random_sample() returns a vector holding random numbers in X and Y. For aperture sampling specifically, the cam:aperture_position attribute (discussed below) proves better for aligning with Blender's standard aperture options.

### Outputs

Three variables must be output:

- position : a point containing the ray origin.

- direction : a vector containing the normalized ray direction.

- throughput : a color specifying the ray's weighting factor, dimming or tinting camera-visible color.

Both position and direction work in camera coordinates, where the origin sits at the camera position, positive Z points along the view direction, and positive Y indicates up.

A black throughput causes the ray to be skipped, useful for marking invalid rays in panoramic mappings.

### Attributes

Camera shaders lack traditional shader features like closures or geometry attributes. Instead, custom attributes are available via getattribute() :

cam:sensor_size
Camera sensor size in millimeters, set in Camera properties.

cam:image_resolution
Rendered image resolution.

cam:focal_distance
Focal distance in millimeters, set in Depth of Field properties.

cam:aperture_aspect_ratio
Aperture aspect ratio, set in Depth of Field properties.

cam:aperture_size
Aperture size, set in Depth of Field properties.

cam:aperture_position
Random position on the aperture, accounting for size, shape, and aspect ratio as configured in Depth of Field properties. Note: this shares random numbers with camera_shader_random_sample() , so avoid using both to prevent correlation.

### Derivatives

Certain features like the Wireframe node require derivatives of ray origin and direction relative to image X and Y. Blender automatically computes these via OSL auto-differentiation. For advanced cases where you compute derivatives more efficiently, define dPdx , dPdy , dDdx , and dDdy outputs. If present, their values override auto-differentiation. Both methods cannot mix—either specify all or none.

[Related references](INDEX.md).
