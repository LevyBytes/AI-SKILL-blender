# Markup Style Guide: text, Document Part

## Markup Style Guide

This page covers conventions for writing Blender's documentation in reStructuredText (RST) markup, which keep the docs clear, consistent, and easy to maintain. General conventions: use three-space indentation; keep lines to 120 characters; use italics for button and menu names; avoid Unicode characters unless strictly necessary; prefer simple sentence structures; and avoid heavily wrapped text, favoring shorter paragraphs and clear sentences. Headings — use this hierarchy:
```text
#################
Document Part
#################

****************
Document Chapter
****************

Document Section
================

Document Subsection
-------------------

Document Subsubsection
^^^^^^^^^^^^^^^^^^^^^^

Document Paragraph
""""""""""""""""""
```
Each .rst file should have only one chapter heading (*), and Parts only on contents or index pages. Basic text styling:
```text
*italic text*
**bold text**
``literal text`` (e.g., filenames, Python code snippets)
```
Interface elements: `:kbd:`LMB`` for keyboard/mouse shortcuts, `*Mirror*` for interface labels (buttons, panels, etc.), and `:menuselection:`3D Viewport --> Add --> Mesh --> Monkey`` for menu navigation paths. Lists — bullet, numbered, and definition:
```text
- First item
- Second item
- Third item
```
```text
#. First step
#. Second step
#. Third step
```
```text
Term
   Definition text here.
```
Useful constructs: `|BLENDER_VERSION|` inserts the version number (e.g. "4.5"); `|BLENDER_VERSION_LABEL|` inserts the version label (e.g. "4.5 LTS"); `:abbr:`SSAO (Screen Space Ambient Occlusion)`` shows the full text on hover; `:term:`Manifold`` links to the Glossary entry; and `:bl-icon:`icon_name`` inlines a Blender icon (full list at Icons). Cross-references and links — internal doc links, explicit section labels, implicit same-document references, and external links:
```text
:doc:`Link Title </path/to/page>`
```
```text
.. _my-section-label:

Section Title
=============

Reference this section later with :ref:`Optional Title <my-section-label>`
```
```text
Section Title
=============

Reference it implicitly later using `Section Title`_
```
```text
`Blender's Official Website `__
```
Context-sensitive manual access: to link Blender UI properties and operators to manual entries: right-click the property/operator in Blender and choose Online Python Reference to get the RNA tag (shown in the OS console), then use an external reference matching that RNA tag:
```text
.. _bpy.types.FluidDomainSettings.use_fractions:

Fractional Obstacles
   Enables finer resolution in fluid/obstacle regions.
```
For operators:
```rst
.. _bpy.ops.curve.subdivide:

Subdivide
=========
```
Blender uses these tags to link UI elements directly to documentation entries via the "Online Manual" option. Admonitions — special blocks highlighting notes, warnings, or extra information; common types are note, tip, important, warning, caution, and seealso, created like:

[Related references](INDEX.md).
