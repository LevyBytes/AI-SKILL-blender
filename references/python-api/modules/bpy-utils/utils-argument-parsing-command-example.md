# bpy.utils: argument parsing command example

Using Python Argument Parsing

The following example demonstrates pairing Python's argparse module with a custom command.

argparse is usually worth reaching for, since it brings a lot of handy utilities and
produces a --help message for your command automatically.

```python
import os
import sys

import bpy

def argparse_create():
    import argparse

    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]) + " --command keyconfig_export",
        description="Write key-configuration to a file.",
    )

    parser.add_argument(
        "-o", "--output",
        dest="output",
        metavar='OUTPUT',
        type=str,
        help="The path to write the keymap to.",
        required=True,
    )

    parser.add_argument(
        "-a", "--all",
        dest="all",
        action="store_true",
        help="Write all key-maps (not only customized key-maps).",
        required=False,
    )

    return parser

def keyconfig_export(argv):
    parser = argparse_create()
    args = parser.parse_args(argv)

    ### Ensure the key configuration is loaded in background mode.
    bpy.utils.keyconfig_init()

    bpy.ops.preferences.keyconfig_export(
        filepath=args.output,
        all=args.all,
    )

    return 0

cli_commands = []

def register():
    cli_commands.append(bpy.utils.register_cli_command("keyconfig_export", keyconfig_export))

def unregister():
    for cmd in cli_commands:
        bpy.utils.unregister_cli_command(cmd)
    cli_commands.clear()

if __name__ == "__main__":
    register()
```

[Related references](INDEX.md).
