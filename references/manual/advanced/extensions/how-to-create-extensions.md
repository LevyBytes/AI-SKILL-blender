# How to Create Extensions

## How to Create Extensions

Creating an extension takes only a few steps: open the directory holding the add-on code or theme file, add a blender_manifest.toml with the required metadata (name, maintainer, ...), and use the Blender command-line tool to build the .zip. To publish to the Blender Extensions Platform, Install from Disk to confirm it works, then upload the .zip (requires a Blender ID); it's held for review and published once the moderation team approves. Extension files: an extension ships as a .zip holding a manifest plus other files, the exact set depending on type. An add-on extension needs at least the manifest and an __init__.py (more complex ones add .py files or wheels):
```text
my_extension-0.0.1.zip
├─ __init__.py
├─ blender_manifest.toml
└─ (...)
```
A theme extension needs only the manifest and the .xml theme file:
```text
my_extension-0.0.1.zip
├─ blender_manifest.toml
└─ theme.xml
```
Extensions may optionally keep all files inside a folder within the archive (common when saving a repository as ZIP from a version-control platform). Manifest: the file carrying all the metadata needed to process an extension. A good starting blender_manifest.toml for the .zip:
```toml
schema_version = "1.0.0"

# Example of manifest file for a Blender extension
# Change the values according to your extension
id = "my_example_extension"
version = "1.0.0"
name = "My Example Extension"
tagline = "This is another extension"
maintainer = "Developer name"
# Supported types: "add-on", "theme"
type = "add-on"

# # Optional: link to documentation, support, source files, etc
# website = "

# # Optional: tag list defined by Blender and server, see:
# # 
# tags = ["Animation", "Sequencer"]

blender_version_min = "4.2.0"
# # Optional: Blender version that the extension does not support, earlier versions are supported.
# # This can be omitted and defined later on the extensions platform if an issue is found.
# blender_version_max = "5.1.0"

# License conforming to  (use "SPDX: prefix)
# 
license = [
"SPDX:GPL-3.0-or-later",
]
# # Optional: required by some licenses.
# copyright = [
# "2002-2024 Developer Name",
# "1998 Company Name",
# ]

# # Optional: list of supported platforms. If omitted, the extension will be available in all operating systems.
# platforms = ["windows-x64", "macos-arm64", "linux-x64"]
# # Other supported platforms: "windows-arm64", "macos-x64"

# # Optional: bundle 3rd party Python modules.
# # 
# wheels = [
# "./wheels/hexdump-3.3-py3-none-any.whl",
# "./wheels/jsmin-3.0.1-py3-none-any.whl",
# ]

# # Optional: add-ons can list which resources they will require:
# # * files (for access of any filesystem operations)
# # * network (for internet access)
# # * clipboard (to read and/or write the system clipboard)
# # * camera (to capture photos and videos)
# # * microphone (to capture audio)
# [permissions]
# network = "Need to sync motion-capture data to server"
# files = "Import/export FBX from/to disk"
# clipboard = "Copy and paste bone transforms"

# # Optional: advanced build settings.
# [build]
# paths_exclude_pattern = [
# "__pycache__/",
# "/.git/",
# "/*.zip",
# ]
```
Required values: blender_version_min (minimum supported version — use at least 4.2.0); id (a unique identifier); license (a list of SPDX license identifiers); maintainer; name (the full name); schema_version (the file-format version — use 1.0.0); tagline (a one-line description up to 64 characters, no trailing punctuation); type ("add-on" or "theme"); and version (following semantic versioning). Optional values: blender_version_max (the unsupported version, earlier ones supported); website; copyright (required by some licenses, formatted "Year Name" or "Year-Year Name"); tags (from the available list); platforms (omitted means all OSes; choices are "windows-x64", "windows-arm64", "macos-x64", "macos-arm64", "linux-x64"); wheels (relative paths to Python wheels); and permissions (the resources an add-on needs — files, network, clipboard, camera, microphone — each with a short single-sentence explanation up to 64 characters, no end punctuation). Optional "build" values, used only by the build subcommand: paths (manifest-relative file paths to include) and paths_exclude_pattern (gitignore-compatible patterns to exclude, which can't be set alongside paths); without a [build] table the default is
```python
[build]
paths_exclude_pattern = [
  "__pycache__/",
  ".git",
  "*.zip",
]
```
[build.generated] is reserved for internal use and must not appear in a TOML. Every value present in the manifest must be filled (no empty string "" or empty list []); simply omit any optional value you don't want.

Extensions can be built, validated, and installed from the command line. Build the package defined in the current directory with `blender --command extension build` (see the build docs). Validate the manifest without building via `blender --command extension validate`, and you can validate a package without extracting it first with `blender --command extension validate add-on-package.zip` (see the validate docs and the Extensions Command Line Arguments). To automate publishing updates on the Extension Platform, see the CI/CD documentation, and to host extensions yourself, see the Creating an Extensions Repository docs.

[Related references](INDEX.md).
