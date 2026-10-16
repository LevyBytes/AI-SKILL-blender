# Viewport Shading

## Viewport Shading

Reference — Mode: All Modes. Location: Header ‣ Viewport Shading. Shortcut: Z, Shift-Z.

Blender ships several shading modes suited to different jobs — Solid works well for modeling, for example, while Rendered helps when setting up lighting. The radio buttons switch mode, and the drop-down opens a popover of extra options below. Pressing Z brings up a pie menu of modes, and Shift-Z flips between your current mode and Wireframe.

Wireframe — draws only the objects' edges.
Wireframe Color — how wireframes are tinted; affects both the Wireframe shading mode and the overlay.
  Theme — uses the Active Object, Wire, or Wire Edit theme color according to the object's state.
  Object — uses the color from the object's Viewport Display settings.
  Random — gives each object a random color.
Background — how the 3D Viewport's backdrop is drawn.
  Theme — uses the theme background, configurable under 3D Viewport ‣ Theme Space ‣ Gradient Colors in the Themes Preferences.
  World — uses the World's Viewport Display color.
  Custom — picks a custom backdrop color.
Options:
  X-Ray (Alt-Z) — makes objects transparent so you can see and select items otherwise hidden behind them; the slider sets opacity.
  Outline — draws an outline around objects, with an adjustable color.

Solid — drives the 3D Viewport through the Workbench Render Engine, showing solid geometry with simplified shading and lighting and no shader nodes. It's strong for modeling and sculpting, with plenty of options to bring out specific geometric features.
Lighting — how light is computed.
  Flat — skips lighting entirely and renders the scene's base color.
  Studio — lights objects with studio lights, configured in the preferences; these can track the camera or stay fixed, and when fixed their angle is adjustable.
    World Space Lighting — uses world-space lighting so the lights don't follow the view camera.
    Rotation — the studio lights' rotation about the Z axis.
  MatCap — lights the scene with a material capture; MatCaps flip horizontally via the Flip MatCap button, and custom ones load in the preferences.
Object Color — where viewport objects take their color from.
  Material — the per-material color from the Viewport Display Material panel.
  Object — the per-object color from the Viewport Display Object panel.
  Random — a random color per object.
  Attribute — the object's active Color Attribute; with none active it falls back to the Viewport Display Object panel color.
  Texture — takes its color out of the active image-texture node, sampled via the active UV map; with no active texture it falls back to the Viewport Display Material panel.
  Custom — one chosen color for the entire scene.
Background — how the 3D Viewport's backdrop is drawn.
  Theme — the theme background, configurable under 3D Viewport ‣ Theme Space ‣ Gradient Colors in the Themes Preferences.
  World — the World's Viewport Display color.
  Custom — a custom backdrop color.
Options:
  Backface Culling — hides the back sides of faces via backface culling.
  Outline — draws an outline around viewport objects, with an adjustable color.
  Specular Highlighting — renders specular highlights. Note: available only when Lighting is Studio, or when the chosen MatCap carries a specular pass.
  X-Ray (Alt-Z) — renders the scene transparent, with the slider controlling how transparent it looks.
  Shadow — casts a crisp shadow into the scene.
    Darkness — how dark that shadow renders, from 0 (invisible) to 1 (black).
    Shadow Settings: Direction controls the shadow-casting light's direction; Offset sets the shadow termination angle and can curb self-shadowing artifacts; Focus governs the falloff at the shadow's edge.
  Depth of Field — applies the active camera's Depth of Field settings in the viewport; visible only while looking through the camera. The settings live on the Properties ‣ Camera ‣ Depth of Field panel.
  Cavity — accentuates ridges and valleys in the scene's geometry.
    Type — the method used to compute cavity. World is more accurate but slower; Screen is fast but ignores the size of the ridges and valleys; Both applies the two methods together.
    Ridge — controls how visible the ridges are.
    Valley — controls how visible the valleys are.

Material Preview — renders the 3D Viewport with EEVEE plus an HDRI environment, making it well-suited to previewing materials and painting textures, since you can swap lighting conditions to test materials. Note: it's unavailable when the scene's render engine is Workbench.
Lighting:
  Scene Lights — uses the scene's lights; when off (or with no lights present) a virtual light fills in.
  Scene World — uses the scene's World; when off, a world is built from the options below.
  HDRI Environment — the environment map lighting the scene.
  Rotation — the environment's rotation about the Z axis.

World Space Lighting — pins the lighting rotation so it no longer follows the camera.
Strength — the environment's light intensity.
World Opacity — how opaque the HDRI is as a backdrop in the viewport.
Blur — a factor that defocuses the HDRI; note this changes only the backdrop's look, not how the lighting diffuses.
Render Pass — instead of the combined render, displays one specific render pass, which helps when analyzing or debugging geometry, materials, and lighting.
Compositor — when to preview the compositing result in the 3D Viewport.
  Disabled — never show the compositing output.
  Camera — show it only in Camera View, the spot that best previews how the final image will look.
  Always — always show the compositing output.

Rendered — renders the 3D Viewport through the scene's Render Engine for interactive rendering, previewing the final pre-composite result including scene-lighting effects. Its options match Material Preview, except that the Render Pass selector offers a different set of passes when the scene uses the Cycles render engine.

[Related references](INDEX.md).
