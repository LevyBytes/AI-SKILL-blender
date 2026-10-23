# Depth of Field

## Depth of Field

Depth of Field: Focus and Blur

EEVEE renders with a pinhole camera model by default, which produces perfectly focused images. To simulate real camera optics, depth of field can be applied via post-process filtering and sample-based methods. Camera optical settings are in the camera properties; quality controls are here.

Note
Depth of field in the 3D Viewport only functions in Camera View.

The post-process method operates in two stages. Stage one uses a blur that works generally but produces poor bokeh on bright highlights. Stage two is sprite-based and enhances bright highlight quality. Sprites are too slow for full-image application; only bright isolated areas receive this treatment. Adjust affected pixels via Sprite Threshold and Neighbor Rejection.

The sample-based method randomizes camera position per sample. More accurate but requires many samples for smooth results. Post-process blur scales down to remove under-sampling artifacts. Some scenes may need extra post-process blur to hide sample patterns; the Overblur option increases blur radius while reducing bokeh sharpness.

Reference
Panel: Render ‣ Depth of Field

Max Size
Maximum depth of field post-process radius in pixels (lower is faster). Zero disables post-process but preserves sample-based method.

Sprite Threshold
Minimum pixel brightness for sprite-based depth of field consideration. Higher values improve performance but reduce highlight quality. Brightness is scene-referred.

Neighbor Rejection
Maximum intensity for sprite neighborhood evaluation. Set this to a brightness level above which visual differences are imperceptible after color management. Lower values improve performance but reduce highlight quality. Brightness is scene-referred.

Jitter Camera
Vary camera position per render sample to boost precision. This may alter actual sample count.

Note
Sample count can increase rapidly.

Hint
Sample count is calculated as:

[sample_count = (ring_count^2 + ring_count) * 3 + 1]

where (ring_count) is the hexaweb pattern ring count. The (ring_count) value ensures the entire pattern includes at least the configured Render Settings sample count.

Over-blur
Scale post-process depth of field radius to suppress artifacts. Higher values blur bokeh shape.

See also
Limitations.

[Related references](INDEX.md).
