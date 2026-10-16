# Introduction

### Introduction

View Layers allow you to separate a render into multiple layers, which can then be composited together. This is useful for rendering scene elements independently—such as characters, lighting variations, or background elements—without duplicating the entire scene or re-rendering everything after each change.

For example, you can:

- Apply different compositing effects to foreground and background elements.

- Render characters separately from the environment for post-processing.

- Generate multiple lighting passes without modifying the original scene setup.

View Layers also improve performance and flexibility during iteration by letting you re-render only the layers that have changed.

View Layers and collections.

Each View Layer references a combination of Collections, which define the visibility, selectability, and contribution of scene objects in the final render. Multiple View Layers can use the same or different collections, allowing for tailored layer setups.

### Selecting View Layers

At the top of the View Layer Properties tab is a list of all View Layers in the active scene.

View Layers list.

Name
The name of the active View Layer. Click to edit.

Add View Layer
Adds a new View Layer to the scene.

- New : Adds an empty View Layer.

- Copy Settings : Duplicates the current View Layer, including collection visibility and overrides.

- Blank : Adds a new View Layer with all collections disabled.

Remove View Layer
Deletes the selected View Layer from the scene.

Note

Each scene must contain at least one View Layer.

### Usage

### Visibility Management

Each Scene consists of one or more Collections. Collections can be enabled or disabled per View Layer, allowing you to control what appears in each layer's render.

This makes it easy to separate lighting, characters, props, or effects into their own passes.

Collection visibility for each View Layer can be adjusted in the Outliner or Collection View Layer Properties.

View Layer collections in the Outliner.

From the Outliner, you can:

- Enable or disable collections per View Layer.

- Set holdout and indirect-only options (Cycles only).

- Manage what objects contribute to the render or compositing.

### Rendering & Compositing

When a scene is rendered, each View Layer is available in the Compositor using the Render Layers Node. This allows you to process each layer independently, combining or adjusting them to create the final output.

Each View Layer can output multiple Render Passes including:

- Combined (final image)

- Diffuse, Glossy, Transmission components

- Shadow, Mist, Ambient Occlusion

- Cryptomatte and Object/Material/ID Masks

- Data passes like Normal, UV, and Depth

These passes make it possible to perform detailed color grading, masking, relighting, and other post-processing operations in a non-destructive workflow.

[Related references](INDEX.md).
