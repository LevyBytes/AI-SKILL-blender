# Installation on Windows

## Installation on Windows

This guide covers installing Python (used to "convert" the source files to HTML), installing Git and downloading the repository, and setting up the build environment. Installing Python — download the Python installation package for Windows (this guide uses version 3.9.x); run the installation wizard, and be sure to enable the "Add Python to PATH" option, which must be on so the make script can build the manual, leaving the other settings at their defaults. Installing Git and downloading the repository — this guide uses the official Git client, though any client works: download and install Git for Windows, then check out the Blender Manual's repository with:
```console
cd ~
git lfs install
git clone https://projects.blender.org/blender/blender-manual.git
```
The download may take a few minutes by connection speed. (With a graphical Git client, just put the repository address in the URL field:)
```text
https://projects.blender.org/blender/blender-manual.git
```
Setting up the build environment: open a Terminal, enter the blender-manual folder git clone just made, and install dependencies:
```console
cd C:\blender-manual
make setup
```
On success you should see this when it finishes:
```text
Successfully installed Jinja2 MarkupSafe Pygments Sphinx docutils sphinx-rtd-theme Cleaning up...
```
Some warnings during setup are harmless, but errors may cause problems. Re-run this command now and then to keep dependencies current. The make setup step automatically creates a virtual environment to avoid touching the system Python (per PEP 668):
```console
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt
```
and the Sphinx command is then at `.venv/Scripts/sphinx-build`.

[Related references](INDEX.md).
