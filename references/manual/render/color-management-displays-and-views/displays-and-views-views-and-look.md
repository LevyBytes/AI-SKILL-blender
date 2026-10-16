# Displays and Views: Views, Look, Exposure, Gamma, Curves

### Views 

Different ways to read the same image on one display.

Standard :

Beyond the display conversion itself it adds nothing. A frequent pick for non-photorealistic work or for video editing where the source already carries its own baked look.

ACES 1.3 :

The ACES view transforms,
a film-and-TV production mainstay. A good fit where you want photorealism.

ACES 2.0 :

The ACES view transform at version 2.0, wearing a more neutral look. Its tone scale eases off, dropping mid-tone contrast and softening highlight rolloff, while gamut mapping improves.

Khronos PBR Neutral :

A tone mapping transform aimed squarely at PBR color accuracy, so the render's output sRGB colors track the materials' input sRGB base color as closely as they can under gray-scale lighting. Its target is product photography, where exposure is even and HDR values keep to tiny specular highlights.

AgX :

A tone mapping transform that outdoes Filmic for more photorealistic output. AgX serves up 16.5 stops of dynamic range and bleeds saturation from heavily exposed colors to echo film's natural answer to light.

Filmic :

A tone mapping transform built for high dynamic range colors. Filmic is deprecated; AgX supersedes it and copes better with saturated colors.

Filmic Log :

Recasts the image into Filmic log color space. Good for handing off to color grading apps, or for studying an image by flattening its darkest and brightest stretches.

False Color :

Paints a heat map of image intensities, putting the dynamic range on view and helping you nail exposure.

The table that follows maps each band of normalized linear color data to the hue False Color paints it.

| Luminance Value | Color |
| --- | --- |
| Low Clip | Black |
| 0.0001% to 0.05% | Blue |
| 0.05% to 0.5% | Blue-Cyan |
| 0.5% to 5% | Cyan |
| 5% to 16% | Green-Cyan |
| 16% to 22% | Gray |
| 22% to 35% | Green-Yellow |
| 35% to 55% | Yellow |
| 55% to 80% | Orange |
| 80% to 97% | Red |
| High Clip | White |

Raw :

For studying an image, not for final export. Raw gives you the image with no color space conversion whatsoever.

### Look 

Pick an artistic effect drawn from measured film response data that loosely echoes the look of particular film stocks. It lands ahead of color space conversion.

### Exposure 

Rides the picture's brightness, in stops, before color space conversion runs.
It is calculated as follows: \(output\_value = render\_value × 2^{(exposure)}\)

### Gamma 

One more gamma correction, this one landing after color space conversion.
Since the default display transforms already do the right conversion, it mostly stands by as an artistic tweak.

### Curves 

Reach for RGB Curves to steer the image's colors ahead of color space conversion.
Read more about using the Curve Widget.

[Related references](INDEX.md).
