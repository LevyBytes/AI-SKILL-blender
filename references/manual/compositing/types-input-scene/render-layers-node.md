# Render Layers Node

## Render Layers Node

The Render Layers node renders a View Layer and pulls its Passes into the compositing graph. It has no input sockets. Properties: Scene (the scene to render a view layer for) and View Layer (the view layer to render, with the adjacent button re-rendering it immediately). A hint notes that to use another scene's compositing output rather than its raw render, first render that scene into multi-layered images (e.g. OpenEXR), then load them into the current scene's Compositor with the Image Node. Outputs: Image (the rendered image), Alpha (the alpha channel), and render-pass sockets (one per enabled pass) — and the viewport compositor only supports render passes with EEVEE, leaving them empty for other engines.

[Related references](INDEX.md).
