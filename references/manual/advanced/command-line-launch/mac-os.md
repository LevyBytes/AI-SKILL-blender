# MacOS

## macOS

macOS quick start: open the Terminal app and run the executable inside the app bundle:
```console
cd /Applications/Blender.app/Contents/MacOS
./Blender
```
If you do this often, add that directory to your PATH: open a Terminal, run `sudo nano /etc/paths`, enter your password, go to the file's bottom, add /Applications/Blender.app/Contents/MacOS, press Ctrl-X to quit, and Y to save — a new terminal will then accept `Blender`. On macOS, ".app" applications are really folders that Finder shows as files, so to get terminal output you must point at the executable inside, which lives at ./Blender.app/Contents/MacOS/Blender (start a terminal from Applications ▸ Utilities). With Blender in the Applications folder you can run `/Applications/Blender.app/Contents/MacOS/Blender`.

[Related references](INDEX.md).
