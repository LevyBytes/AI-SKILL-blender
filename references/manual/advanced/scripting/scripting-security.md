# Scripting & Security

## Scripting & Security

Scripting and security. Embedding Python in blend-files is valuable for advanced work like rigging and automation, but it's a security risk since Python doesn't limit what a script can do, so only run scripts from sources you trust. Automatic execution is off by default, though some blend-files need it; when a blend-file tries to run a script and isn't allowed, a dialog lets you Allow Execution or Ignore the scripts. Scripts in blend-files — auto execution happens via registered text-blocks (a text data-block with its Register option on loads at startup) and animation drivers (Python expressions that drive values, common in advanced rigs and animation). Manual execution: some scripts run only with user interaction, so they execute even with auto-execution off, but be aware they're not always obvious — running a script in the Text editor, or rendering with Freestyle (which uses scripts to control line styles). Controlling script execution: the File Browser has a Trusted Source option for case-by-case control of auto execution, and because you might forget it or open a file without the browser, you can change the default. Setting defaults: the Preferences "Auto Run Python Scripts" toggle makes Trusted Source on by default and lets scripts run when blend-files load outside the File Browser; once on, you can exclude certain directories, a typical setup being to trust every path except the download directory. Command line: for batch rendering or other UI-less tasks the Preferences still apply but can be overridden — enable with -y or --enable-autoexec, disable with -Y or --disable-autoexec. For example, to render an animation in background mode while allowing drivers and other scripts:
```console
blender --background --enable-autoexec my_movie.blend --render-anim
```
These arguments also work when starting a normal Blender instance and still override the Preferences.

[Related references](INDEX.md).
