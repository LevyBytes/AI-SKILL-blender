# Markup Style Guide: text, .. note

```text
.. note::

   This is a note for general information.
```
Swap note for any other type in the list. Images — use the figure directive with captions:
```text
.. figure:: /images/interface_splash_current.webp

   Splash screen of Blender.
```
Screenshots guidelines: use Blender's default theme and settings; zoom to maximum (Ctrl-MMB or NumpadPlus); zoom out exactly eight steps (NumpadMinus pressed eight times); and leave about a 30-pixel margin around the content where applicable. File naming: lowercase letters, no spaces, underscores between sections and dashes within multi-word sections; place images only in manual/images (no subfolders) — e.g. interface_splash_current.png, modeling_meshes_edit-mode.png. Image formats: .png for interface screenshots or solid-color images; .jpg for photos or high-color-variation renders; avoid .gif, using embedded videos for animations instead. Videos — embed videos hosted on Blender's PeerTube at video.blender.org:
```text
.. peertube:: ID
```
The ID comes from the video URL, e.g. for https://video.blender.org/videos/watch/47448bc1-0cc0-4bd1-b6c8-9115d8f7e08c the ID is 47448bc1-0cc0-4bd1-b6c8-9115d8f7e08c. Guidelines for videos: prefer videos without spoken or on-screen text for easier translation, and don't rely on videos alone — the manual text should clearly document the process. Code samples — use syntax highlighting and optional line numbering:
```text
.. code-block:: python
   :linenos:

   import bpy

   def example_function():
       print("Hello Blender")
```
Placeholders and editor notes — for content needing later updates: reader-visible todo or internal (hidden) notes:
```text
.. todo:: Complete this section when feature is finalized.
```
```text
.. Internal developer reminder goes here
```
Further reading: the Sphinx RST Primer (an introduction to RST syntax) and the Docutils reStructuredText Reference (comprehensive RST markup documentation).

[Related references](INDEX.md).
