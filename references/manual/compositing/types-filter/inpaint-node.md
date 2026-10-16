# Inpaint Node

## Inpaint Node

The Inpaint node extends an image's borders into transparent or masked regions, useful for problems like "wire removal" and holes left by chroma keying. Inputs: Image (standard color input) and Size (how many times to extend the image). Output: Image (standard color output). Examples: after chroma keying removes a "wire," you're left with a blank space (shown as a black line, but alpha in your output), and inpainting fills a few pixels from the surrounding image to remove the wire — but the wider the hole, the more noticeable the effect, so using more than a few pixels of infill is about as irritating as the wire; it can also cover other minor sins like motion-capture control points, so use it sparingly.

[Related references](INDEX.md).
