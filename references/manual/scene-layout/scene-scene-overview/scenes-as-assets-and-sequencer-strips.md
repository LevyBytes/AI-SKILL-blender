# Introduction: Scenes as Assets, Scenes in the Video Sequencer

### Introduction

Scenes organize your projects. A single blend-file supports multiple scenes,
which can exchange data such as objects, materials, and collections.

A scene establishes the rendered elements, active viewing angle, light arrangement,
and output parameters that comprise a production component.
For instance, a single blend-file might contain multiple scenes representing various shots,
light configurations, or workflow phases.

Scene administration and library connections are grounded in Blender's
Library and Data System.
Prior familiarity with data-block concepts, linking, and importing
is beneficial before proceeding.

### Scenes as Assets

Scenes can be flagged as Assets and applied in other projects.
This enables their display in the Asset Browser for reuse.

Scene assets serve as handy instruments for managing preset scene structures, illumination configurations, or compositional templates.
They retain all pertinent information (including cameras, lights, and output parameters) and can be moved into any accessible Blender
document.

When a scene asset is brought into another interface (excluding the Asset Browser alone),
Blender carries out one of the following operations:

- Link or Append: Incorporates the scene into the current blend-file as a linked or imported data-block.

- Activate: Establishes the added (or connected) scene as the presently operating one in the interface.

Scene assets generate preview visuals mechanically by rendering with the primary camera in Solid Display mode.
The scene must feature a designated camera for this to work.

Typical applications for scene assets encompass:

- Building replicable lighting or workspace configurations.

- Saving shot arrangements for multi-shot works.

- Maintaining consistent output parameters across documents.

- Creating foundational frameworks for new documents or teams.

### Scenes in the Video Sequencer

Scenes can also act as Scene Strips within the
Video Sequencer.
This allows combining or editing multiple scenes together in one playback sequence.

For illustration, individual frames of an animated sequence might inhabit separate scenes,
which are subsequently organized in a master scene employing scene strips to arrange them sequentially.
This technique proves valuable for multi-shot work, promotional content,
or arrangement tasks without demanding intermediate output stages.

When deployed as strips, scenes render dynamically through playback or output,
and they employ shared data-blocks unless produced as complete duplicates.

[Related references](INDEX.md).
