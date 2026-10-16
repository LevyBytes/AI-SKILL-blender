# Usage: Multi-View and Stereo 3D Image I/O, Image Editor, Compositor

### Multi-View and Stereo 3D Image I/O 

Multi-View and Stereo 3D
Multi-view images can be exported in formats aligned with production needs. Default behavior saves each view separately, creating as many files as views rendered. For stereo 3D delivery or interim assessments, stereo 3D-ready images matching display modes are convenient. Available formats correspond to window display options.

Lossy-Formats
Certain stereo 3D formats incur substantial data reduction. Anaglyph strips entire color channels. Top-Bottom compressed removes vertical resolution data. Interlace applies considerable compression. These formats can be re-imported to Blender and treated as stereo 3D when the window display mode aligns with image format.

Lossless Formats
Selected formats retain full information with zero export/import penalties. Individual files (saved as lossless like PNG or OpenEXR) load back with no degradation. For stereo 3D formats, lossless preservation occurs only with Top-Bottom and Side-by-Side modes lacking the Squeezed Frame option.

Multi-View OpenEXR
Multi-view OpenEXR stores multiple camera views in one file while maintaining backward compatibility with standard OpenEXR readers (showing one view). Multi-view native support is exclusive to OpenEXR format.

### Image Editor 

View Menu
Stereo 3D-rendered output displays either combined stereo 3D results or individual camera views in the Image Editor. This applies to Viewer nodes, render results, and opened images.

Stereo 3D and view menu. 

Views Format
Importing images into the Image Editor initially loads them as individual images. For Stereo 3D format images, configure interpretation via Views Format toggle and Multi-View activation with the matching stereo method.

Views formats and stereo 3D. 

### Compositor 

Multi-view handling is seamless in the Compositor. Single-view composition finishes before remaining views are processed. Workflow mirrors single-view operation, with support for multi-view format images, video, and sequences.

Compositor, backdrop and Split Viewer node. 

Render views are defined in the scene's current views configuration, parallel to how composite output resolution is configured at the scene render level, independent of Image node resolution or Render Layers from alternate scenes.

Note

Single-View Images

If an Image node references a view absent from the render target, the image is handled as single-view.

Switch View Node
Use the Switch View node when separating views is necessary, combining them before an Output node.

Tip

Performance

During GUI rendering and compositing, all views process before composition. Testing iterations benefit from disabling all but one view in the Scene Views panel, then re-enabling all afterward.

[Related references](INDEX.md).
