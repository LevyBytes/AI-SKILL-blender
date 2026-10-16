# Sequencer Strip Info Node

## Sequencer Strip Info Node

The Sequencer Strip Info node returns information about the Video Sequencer strip the Compositor modifier is applied to, including timing and transform data like frame range, position, rotation, and scale. Note it's only supported when the Compositor runs in the Video Sequencer's context (e.g. a Compositor modifier on a strip), outputting default values otherwise. It has no input sockets. Outputs: Start Frame and End Frame (the strip's start/end in the Sequencer timeline), Location (its 2D position offset, from its transform), Rotation (its rotation, from its transform settings), and Scale (its X/Y scale, from its transform settings).

[Related references](INDEX.md).
