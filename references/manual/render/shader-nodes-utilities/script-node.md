# Script Node

## Script Node

### Script Node

Cycles Only

This node enables integration of custom shaders developed in Open Shading Language (OSL) within the Cycles rendering engine. It functions as a connection point between OSL shader implementations and Blender's node-based shading workflow.

Each Script node represents one OSL shader, with parameters derived from the code. Shaders may reside within the blend file itself or be loaded from external sources.

Technical artists and shader developers benefit from this feature when they require precise control over material behavior beyond standard node capabilities.

Note

The Script node only executes if Open Shading Language is activated.

Tip

For production pipelines, wrap script nodes in a node group and link it across blend-files. This approach simplifies future modifications, as socket changes do not require updates in every dependent file.

### Properties

Mode
Specifies how to reference OSL shader code.

Internal :

A text data-block stores the shader, with compiled bytecode embedded in the node. Useful for distributing self-contained blend files.

Script Node Update
Recompiles the text data-block and regenerates inputs/outputs as necessary.

External :

Loads a .osl file from disk, automatically compiling it into a .oso file in the same location. Alternatively, point directly to a pre-compiled .oso file. A third option references the module name within the shader search path.

The shader search path is located alongside scripts and configuration:

Linux:

`$HOME/.config/blender/5.1/shaders/`

Windows:

`C:\Users\$user\AppData\Roaming\Blender Foundation\Blender\5.1\shaders\`

macOS:

`/Users/$USER/Library/Application Support/Blender/5.1/shaders/`

[Related references](INDEX.md).
