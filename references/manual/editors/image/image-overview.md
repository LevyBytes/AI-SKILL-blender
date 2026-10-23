# Introduction

The Image Editor lets you create, view, and edit images, and also see render results and intermediate Compositor output.

Toolbar:
Sample: reads the color of one or more pixels; while you hold LMB the footer shows the cursor's X and Y, the color in RGBA, the color in RGB after Color Management, the color in HSV, and the Luminance.
Sample Size: the side length of the square used to sample underlying pixels; above 1, the result averages all the pixels it covers.
Annotate: see Annotations.

Header - Mode: View (displays images), Paint (Texture Paint), Mask (Masking).
View: tools for how content is shown in the editor (see Navigating).
Image: tools for opening and manipulating images; an asterisk marks unsaved changes (see Editing Images).
Image — a data-block menu for choosing images; once one is chosen, the Image tab appears in the Sidebar. Beyond loading existing images you can also create new ones — the New Image pop-over's Tiled option makes a UDIM-capable image, and for the rest see Generated Images. The data-block selector also lists Render Result (displays renders; selecting it enables the Slot, View Layer, and Render Pass selectors below) and Viewer Node (displays whatever feeds the Compositor's Viewer Node).
Image Pin: stops the Image Editor from auto-switching to the selected object's texture (which only happens when the 3D Viewport is in Texture Paint mode).
Show Sequencer Scene: appears on the Render Result only when a Sequencer Scene exists and differs from the window's active scene; after a render its state gets picked automatically based on the render type.
Slot: the render slot to view and render into; pick an empty slot before rendering to keep earlier renders, then compare with J and Alt-J to cycle forward and back, or press number keys 1, 2, 3, etc. to jump to a slot. Rename slots by double-clicking their name in the Sidebar's Image panel.
View Layer: which View Layer to show.
Render Pass: which Render Pass to show.
Viewport Gizmos: toggle all gizmos with the button or specific ones via the drop-down.
  Navigate: turns the pan/zoom gizmos for the 2D viewport on or off (see Navigation Gizmos).
Display Channels: choose which color channels appear.
  Color & Alpha: turns on transparency, with a checkerboard shown behind the image.
  Color: disables transparency.
  Alpha: shows the alpha channel in grayscale; white is opaque, black transparent.
  Z-Buffer: shows depth from the camera, between Clip Start and Clip End from the Camera settings.
  Red, Green, Blue: one color channel shown as grayscale.

Asset Shelf Region: depending on the mode, the asset shelf may appear for quick access to mode-specific assets (brush assets in Paint mode, for instance); see Asset Shelf.

Main View: holding RMB samples the image like the Sample tool, except it always reads just one pixel.

[Related references](INDEX.md).
