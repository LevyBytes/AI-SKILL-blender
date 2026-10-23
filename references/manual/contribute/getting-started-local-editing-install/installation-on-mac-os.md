# Installation on macOS

## Installation on macOS

This guide covers installing dependencies, downloading the repository, and setting up the build environment, and relies heavily on command-line tools, assuming little familiarity with the macOS Terminal. Installing dependencies — install or confirm you have PIP, Git, and Git LFS; with Homebrew, run:
```console
python3 -m ensurepip
brew install git git-lfs
git lfs install
```
Downloading the repository: check out the Blender Manual's repository (a few minutes by connection speed):
```console
cd ~
git clone https://projects.blender.org/blender/blender-manual.git
```
Setting up the build environment: open a Terminal, enter the folder git clone made, and install dependencies:
```console
cd ~/blender-manual
make setup
```
Re-run `make setup` periodically to keep dependencies current. It automatically creates a virtual environment to avoid touching the system Python (per PEP 668):
```text
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```
and the Sphinx command is then at `.venv/bin/sphinx-build`.

[Related references](INDEX.md).
