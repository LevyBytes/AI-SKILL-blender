# Troubleshooting Errors & Crashes: sys.exit

### sys.exit

Certain Python modules call sys.exit() on their own when something goes wrong. It's not common, but it's worth knowing about, because sys.exit() shuts Blender down at once and can look as if Blender simply crashed.

The argparse module, for one, prints an error and exits when handed invalid arguments.

One crude debugging trick: assign sys.exit = None , then see which Python line is the one quitting. You could equally replace sys.exit with a function of your own, though manipulating Python this way counts as bad practice.

[Related references](INDEX.md).
