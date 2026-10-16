# Templates

## Templates

This guide gives patterns for documenting interface elements and directories. Operator menus — each operator gets its own heading or page depending on content length, opening with a reference admonition documenting the operator's context:
```text
.. reference::

   :Mode: Edit Mode
   :Menu: :menuselection:`Curve --> Snap`
   :Shortcut: :kbd:`Shift-S`
```
Panels — document each panel under its own heading, with nested panels at decreasing heading levels; a panel may warrant its own page by documentation length or panel count, and expanded menus that toggle which properties show should be treated like subpanels:
```text
Panel Title
===========

Nested Panel Title
------------------
```
Properties — document with definition lists, using nested definitions for properties hidden behind other properties:
```text
Property
   Property description.

   Hidden Property
      Hidden property description.
```
Document select menus like:
```text
Menu Label
   General description of the menu.

   :Menu Item: Menu Item Definition.
   :Menu Item: Menu Item Definition.
   :Menu Item: Menu Item Definition.
```
Nodes — always give three headings (inputs, properties, outputs), noting absence where the node has none, with an optional example(s) section at the end of the page:
```rst
**********
World Node
**********

.. figure:: /images/render_shader-nodes_output_world_node.png
   :align: right

   The World node.

Introduction and general use case(s).

Inputs
======

This node has no inputs.

Properties
==========

This node has no properties.

Outputs
=======

This node has no outputs.

Example
=======
```
Directory layout — structure sections generally as a directory holding index.rst (links to internal files), introduction.rst, then section_1.rst, section_2.rst, and so on; for example:
```text
- rendering/
  - index.rst
  - cycles/
    - index.rst
    - introduction.rst
  - materials/
    - index.rst
    - introduction.rst
    - volumes.rst
```
The idea is to enclose all of a section's content in a folder, ideally with an index.rst (the section's TOC) and an introduction.rst (introducing its contents). Table of contents — by default show two levels of depth:
```text
.. toctree::
   :maxdepth: 2

   introduction.rst
   perspective.rst
   depth_of_field.rst
```

[Related references](INDEX.md).
