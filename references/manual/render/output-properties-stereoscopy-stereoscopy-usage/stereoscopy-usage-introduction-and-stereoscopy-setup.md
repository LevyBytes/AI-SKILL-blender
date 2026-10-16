# Usage: Introduction, Stereoscopy Setup, Camera, Viewport, Stereo 3D Display, Viewport Preview, Rendering and Image Editor, Image Formats, Final Considerations, Window Stereo 3D Display

## Usage

### Usage 

This example transforms an existing monoscopic project into stereo 3D-capable output.

Creature Factory 2 by Andy Goralczyk rendered in stereo 3D (anaglyph).

### Introduction 

Begin by loading your scene, in this case turntable.blend from the Creature Factory 2 Open Movie Workshop series created by the Blender Institute and Andy Goralczyk.

Turntable Creature Factory 2. 

### Stereoscopy Setup 

Access the Output Properties and activate Stereoscopy for your scene.

Scene render views. 

Note

When Stereoscopy is activated, you gain 3D preview capability in the viewport plus new panel areas throughout the interface.

Viewport with 3D visualization. 

### Camera 

Select the camera object in the Outliner. In the Camera panel's Stereoscopy tab, modify the Convergence Distance to fine-tune stereo 3D parameters.

The viewport instantly reflects alterations in real-time, permitting immediate preview of depth values.

Stereo convergence distance. 

### Viewport 

For initial camera setup, establish the convergence plane in the viewport based on your depth structure. Leave camera view mode and the convergence plane becomes immediately visible in front of the camera.

Toggle this setting and other display choices in the Stereoscopy panel of the 3D Viewport's Sidebar. Camera frustum volumes are also viewable in the following scene.

Viewport plane and volume stereo preview. 

### Stereo 3D Display 

On compatible 3D displays, access the Window menu and invoke the Stereo 3D operator to adjust display mode. Understand that some modes require full-screen and impose substantial processing demands.

Window menu, stereo 3D operator. 

### Viewport Preview 

Test your setup by saving a Viewport Preview before final rendering. The Render Output panel permits selection of the output Views Format.

Available options include individual files per camera, stacked layouts, anaglyph, and others. Select the format matching your display setup.

### Rendering and Image Editor 

Upon reaching the target appearance, proceed with final animation export. Use the Image Editor to examine individual camera views and combined stereo results.

### Image Formats 

Your final output can employ more robust storage formats. This example uses side-by-side cross-eyed stereo 3D storage.

Side-by-side cross-eye format. 

### Final Considerations 

As this tutorial illustrates, stereo 3D rendering involves more than frame pairs. Introduction of stereo considerations early in the pipeline streamlines the overall process. The following information provides deeper coverage of individual workflow components encountered here.

### Window Stereo 3D Display 

Proper stereo image presentation forms a core part of the Stereoscopy pipeline. Blender accommodates display hardware ranging from high-end 3D monitors to affordable glasses-based solutions. Additionally, you can configure a distinct display mode per window.

Alter display mode via the Window menu or create custom shortcuts with the wm.set_stereo_3d operator.

Window menu, stereo 3D operator.

[Related references](INDEX.md).
