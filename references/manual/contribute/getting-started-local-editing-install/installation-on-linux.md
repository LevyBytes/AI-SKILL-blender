# Installation on Linux

## Installation on Linux

This guide covers installing dependencies, downloading the repository, and setting up the build environment. Installing dependencies — run the command for your Linux distribution in a terminal. Debian/Ubuntu:
```console
sudo apt-get install python3 python3-pip git git-lfs
git lfs install --skip-repo
```
Redhat/Fedora:
```console
sudo dnf install python python-pip git git-lfs
git lfs install --skip-repo
```
Arch Linux:
```console
sudo pacman -S python python-pip git git-lfs
git lfs install --skip-repo
```
Downloading the repository — check out the Blender Manual's repository (this may take a few minutes by connection speed):
```console
cd ~
git clone https://projects.blender.org/blender/blender-manual.git
```
Setting up the build environment — open a Terminal, enter the folder git clone made, and install dependencies:
```console
cd ~/blender-manual
make setup
```
Re-run `make setup` now and then to keep dependencies current. It automatically creates a virtual environment to avoid touching the system Python (per PEP 668):
```text
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```
and the Sphinx command is then at `.venv/bin/sphinx-build`.

[Related references](INDEX.md).
