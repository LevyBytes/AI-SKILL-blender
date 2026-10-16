# Contribute Documentation: Important Notes, Best Practices for Documentation, Writing Good Examples, Style Guidelines, Testing Your Changes, Contributing Your Changes

```text
"""
Example Title
+++++++++++++

A description of what this example demonstrates.
This doc-string appears above the code in the documentation.

You can use **reStructuredText** formatting here, for example:

- *Italic* text with single asterisks
- **Bold** text with double asterisks
- ``inline code`` with double backticks
- :class:`bpy.types.Operator` to link to API classes
- Links to `external resources `__

.. note::

You can use this to highlight important information.

Everything after this doc-string is included as code.
"""
import bpy

### Example code goes here
print("This is an example")
```

#### Important Notes

- Triple double-quotes """ have to open the file; doc-strings using single quotes go unrecognized.

- For the title, underline the section header with + characters.

- Whatever follows the doc-string is treated as code in the documentation.

- Need more code-blocks separated by text? Add further files.

### Best Practices for Documentation

### Writing Good Examples

- Keep it simple : show a single concept per example.

- Make it runnable : the example ought to work as-is when pasted into the text editor or Python console.

- Use comments : annotate generously, writing as though the reader has never met the APIs or ideas on display.

### Style Guidelines

We're aiming for solid technical writing in the docs. For markup and conventions, lean on these style guides from the User Manual:

- Markup Guide

- Writing Guide

- reStructuredText Primer

### Testing Your Changes

Having added or revised documentation, rebuild it (see Building the Documentation) and keep an eye out for warnings — dead links, references that don't resolve, or formatting problems. Then load the generated HTML in a browser and verify it all renders as it should.

### Contributing Your Changes

With your documentation additions or improvements complete,
open a pull request by following
Blender's contribution guidelines.

[Related references](INDEX.md).
