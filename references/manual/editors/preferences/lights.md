# Lights

## Lights

Studio Lights — these light the 3D Viewport during Solid View and aren't rendered; unlike scene lights, their direction tracks the viewport's orientation.
Editor — you get up to four virtual light sources. The Light toggles switch individual lights on or off, though at least one of the four has to stay enabled for the 3D Viewport. The lights are identical apart from direction and color, and you can set each one's direction along with its diffuse and specular colors.
  Use Light — toggles that light.
  Diffuse — the light's constant color.
  Specular — the light's highlight color.
  Smooth — softens this light's shading, making the lighting less direct.
  Direction — the light's direction (see Direction Buttons); it matches what's shown on the sphere's surface.
  Ambient Color — the color of unlit areas.

MatCaps — this panel handles MatCap image files used to light the view when MatCap shading is on. Two image kinds are supported: regular image files and multilayered OpenEXR files. With multilayered OpenEXR, the "diffuse" layer serves as the diffuse pass and the "specular" layer as the specular pass; regular images count as "diffuse" only and have no specular highlighting. The diffuse pass multiplies the objects' base color and the specular pass adds on top, so MatCaps with only a diffuse pass tend to look metallic, while a separate specular pass lets you fake a wider range of materials.

HDRIs — this panel handles HDRI image files used to light the view when Material Preview or Rendered shading is on.

[Related references](INDEX.md).
