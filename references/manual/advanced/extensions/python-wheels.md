# Python Wheels

## Python Wheels

Python wheels (*.whl) are the standard way to distribute Python modules, and Blender supports them so extensions can be self-contained. Guideline: by convention, keep the files under ./wheels/. Requirements: bundle wheels unmodified from Python's package index; include their dependencies; match Python's binary-distribution filename specification (wheels downloaded from the package index already do); and use forward slashes as path separators when listing them in the manifest. How to bundle: download the wheel into ./wheels/ — for a platform-independent module, `pip wheel jsmin -w ./wheels`, and for one with compiled binaries, fetch a wheel for every supported platform, e.g.:
```console
pip download pillow --dest ./wheels --only-binary=:all: --python-version=3.13 --platform=macosx_11_0_arm64
pip download pillow --dest ./wheels --only-binary=:all: --python-version=3.13 --platform=manylinux_2_28_x86_64
pip download pillow --dest ./wheels --only-binary=:all: --python-version=3.13 --platform=win_amd64
```
(the platform identifiers are listed on pillow's download page). Then list the wheels as paths in blender_manifest.toml:
```python
wheels = [
   "./wheels/pillow-12.1.0-cp313-cp313-macosx_11_0_arm64.whl",
   "./wheels/pillow-12.1.0-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl",
   "./wheels/pillow-12.1.0-cp313-cp313-win_amd64.whl",
]
```
Installing the package then extracts the wheel into the extension's own site-packages directory. To confirm it loads, import it in the Python console and print its location:
```python
import PIL
print(PIL.__file__)
```
Platform builds: wheels can bloat an extension, so you can build a separate zip per required platform using the build command's --split-platforms option, `blender --command extension build --split-platforms`. For example, a manifest excerpt
```python
id = "my_addon_with_wheels"
version = "1.0.0"

platforms = ["windows-x64", "macos-x64"]
wheels = [
   "./wheels/pillow-12.1.0-cp313-cp313-macosx_11_0_arm64.whl",
   "./wheels/pillow-12.1.0-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl",
   "./wheels/pillow-12.1.0-cp313-cp313-win_amd64.whl",
]
```
yields my_addon_with_wheels-1.0.0-windows_x64.zip and my_addon_with_wheels-1.0.0-macos_x64.zip — and even though a Linux wheel is present, no Linux zip is built, because the platforms field lists only Mac and Windows.

[Related references](INDEX.md).
