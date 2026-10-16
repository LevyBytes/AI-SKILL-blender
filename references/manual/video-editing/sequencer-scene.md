# Sequencer Scene

## Sequencer Scene

### Sequencer Scene

The video sequencer relies on a dedicated scene data-block holding the edit. This is the Sequencer Scene.

Separating the sequencer into its own scene offers advantages: managing multiple edit versions in one file, and supporting workflows with different scenes and scene strips. See the section on multi-scene editing and scene strips below.

### Usage

### Creating a Sequencer Scene

To begin with the Sequencer, create or activate an existing Scene.

- Open a workspace including a Video Sequence Editor.

- Click the "New" button in the Sequencer header to make a new Sequencer Scene, or select an existing one.

### Working with Multiple Scenes

The sequencer scene is independent from the active window scene, enabling simultaneous work on scene strips and their referenced scenes within one workspace.

A typical arrangement:

- Workspace combining a Video Sequence Editor and a 3D Viewport.

- Sequencer Scene in the VSE (e.g., titled "Edit").

- Additional scenes for distinct shots or locations.

Add scene strips referencing the existing scenes (or new ones). Then activate Sync Scene Time in the Sequencer Playback Controls. The active scene (and 3D Viewport display) updates to match the current scene strip in the Sequencer.

This arrangement allows rapid scene switching via timeline scrubbing or playback.

### Playback Context

Since the Sequencer Scene is separate from the active scene, playback depends on context. Sequencer playback shows the Sequencer Scene. Other editors play the active window scene.

### Rendering

Render and output settings for the Sequencer Scene match regular scenes. These appear in the Output tab of the Properties editor. These settings follow the active window scene by default (unless a scene is pinned to the properties).

When the active scene differs from the Sequencer Scene in the workspace, the "Render" menu includes separate options to render the Sequencer Scene (bypassing the active Scene).

[Related references](INDEX.md).
