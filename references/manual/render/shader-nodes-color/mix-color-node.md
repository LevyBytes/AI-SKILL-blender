# Mix Color Node

## Mix Color Node

The Mix Color node mixes value, color, and vector inputs using a factor that controls the interpolation amount, with the Color mode adding blending modes. Inputs: Factor (how much A and B are mixed) and A/B (the two inputs). Properties: Data Type (float, vector, color, or rotation); Factor Mode (Vector only — Uniform, where one float controls the factor, or Non-Uniform, where a vector controls it per XYZ channel); Mix (Color only — the blend mode from the menu; see Color Blend Modes), with options Add, Subtract, Multiply, Screen, Divide, Difference, Darken, Lighten, Overlay, Color Dodge, Color Burn, Hue, Saturation, Value, Color, Soft Light, Linear Light; Clamp Factor (limit the factor to 0.0-1.0, otherwise the node uses Extrapolation); and Clamp Result (Color only — limit the Result to 0.0-1.0). Output: Result (the mix in the chosen data type). Examples — Fixing overexposure: darken an overexposed render and raise contrast — the top RGB Curves node darkens by linearly scaling each value smaller, the bottom one raises contrast by making small values smaller and large ones larger, and a Mix node blends the two. Watermark images: long ago a mark was pressed into drying paper to identify its maker, barely visible except in the right light (an early subliminal advertising); today people watermark images to mark intellectual property, for subliminal advertising, or to track proliferation, and Blender has a full set of tools to encode a watermark and detect one. Encoding: build a personal watermark (a name, word, shape, or hard-to-replicate image — neutral gray works best with this method, but any color or pattern works, from one pixel to a gradient); in the example it's encoded at a specific location via the Translate node (so you only look there later), converted to grayscale with the RGB to BW node, reduced to one-tenth intensity with the Map Range node, and added with the Add node (a Mix node in Add mode) so marked pixels become slightly brighter — scale it less or use a contrasting color if you want it noticed, and experiment with other mix settings and rigs. Decoding: compare a suspect image to your non-watermarked original with the node tree shown, where the Mix node uses Difference and the Map Value node amplifies whatever difference remains, making the original mark clearly stand out.

The Mix Color Node mixes value, color, and vector inputs, using a factor to control the amount of interpolation; the Color mode adds extra blending modes.

Inputs:
Factor — how much mixing happens between the A and B inputs.
A/B — the two inputs mixed together.

Properties:
Data Type — the data type used for mixing; the node supports float, vector, color, and rotation data types.
Factor Mode (Vector only) — set to Uniform or Non-Uniform: Uniform uses a single float for the factor, Non-Uniform uses a vector controlling the factor for each XYZ channel separately.
Mix (Color only) — pick a blend mode from the select menu (see Color Blend Modes for details on each): Add, Subtract, Multiply, Screen, Divide, Difference, Darken, Lighten, Overlay, Color Dodge, Color Burn, Hue, Saturation, Value, Color, Soft Light, Linear Light.
Clamp Factor — limit the factor to between 0.0 and 1.0; unchecked, the node operates using Extrapolation.
Clamp Result (Color only) — limit the Result to between 0.0 and 1.0.

Outputs:
Result — the mix result, in the selected data type.

Examples: below are blending-mode examples plus some practical use cases, such as blending a colored pattern with a flat color (top row) and with a circular mask (bottom row).
Fixing overexposure: the compositing setup fixes an overexposed render by darkening it and increasing contrast. The top RGB Curves Node darkens the image by linearly scaling each color value down; the bottom curve node raises contrast by making small values smaller and large values larger; finally the Mix node blends the two together.
Watermark Images: in the old days a pattern pressed into the paper mush as it dried made a mark identifying who made the paper and where it came from, barely perceptible except in just the right light — probably the first form of subliminal advertising. Nowadays people watermark images to mark them as personal intellectual property, for subliminal advertising of the author or hosting service, or simply to track an image's spread across the web. Blender provides a complete set of tools to both encode your watermark and tell whether an image carries it.
- Encoding your watermark in an image: first build your own watermark — a name, a word, or a shape or image not easily replicated; neutral gray works best with the suggested encoding method, but you may use other colors or patterns, from a single pixel to a whole gradient. In the example, the watermark is encoded at a specific location using the Translate node (so later you only have to look at that spot for the mark), converted to grayscale numbers with the RGB to BW node, then fed into the Map Range node to reduce the mark to one-tenth of its original intensity. The Add node (a Mix node with blending mode Add) adds the corresponding pixels, making the ones holding the mark ever so slightly brighter. Of course, to have people notice the mark, scale it less or use a contrasting color — and there are many other approaches with different mix settings and fancier rigs, so experiment.
- Decoding an image for your watermark: when you see an image you think might be yours, compare it to your non-watermarked stock original with a node tree where the Mix node is set to Difference and the Map Value node amplifies any difference, so the original mark clearly stands out.

### Watermark Images 

Watermarking identifies work ownership or origin. In papermaking, a watermark is an impressed pattern made during drying, marking maker identity. Contemporary digital watermarks establish intellectual property ownership, provide subtle branding, or track distribution.

Blender supplies complete functionality for both embedding and verifying watermarks.

#### Encoding your Watermark in an Image 

Start by creating a personal watermark—text, symbol, or distinctive image hard to replicate. Though neutral gray functions optimally with the proposed technique, any color or pattern works. Size flexibility ranges from single pixel to complete gradient.

Below, we position the watermark using the Translate node; later we need only check a specific area. The RGB to BW node converts the color image to grayscale, fed to Map Range to diminish the mark to one-tenth strength.

The Add node (Mix with Add mode) sums pixel values, making watermarked areas subtly brighter.

Embedding a watermark in an image. 

For visible watermarks, scale less aggressively or use contrasting colors. Many alternate approaches exist with different mix settings and refined rigs. Experimentation is encouraged!

#### Decoding an Image for your Watermark 

When examining suspect images, employ the tree below to compare against your original unmarked copy. The Mix node uses Difference mode to isolate variations, and the Map Value node magnifies contrast. Your watermark stands out distinctly.

Checking an image for your watermark.

[Related references](INDEX.md).
