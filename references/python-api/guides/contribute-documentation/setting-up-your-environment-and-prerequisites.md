# Contribute Documentation: Setting Up Your Environment, Prerequisites, Installing Documentation Requirements, Building the Documentation, Modifying API Documentation, Adding Example Code Snippets, Example File Naming Convention, Example File Structure

## Contribute Documentation

### Contribute Documentation

This page walks through contributing to the Blender Python API documentation — covering how to write examples, how to format the docs, and how to build them on your own machine.

### Setting Up Your Environment

### Prerequisites

A few things have to be in place before a build:

Blender Source Code
Pull down a clone of the Blender repository, working from the
official build instructions.

Python Environment (optional)
Get a Python virtual environment going.

### Installing Documentation Requirements

The usual route is to spin up a virtual environment and install whatever is listed in doc/python_api/requirements.txt . That said, Sphinx is the lone hard dependency, and you can grab it on its own:

```console
pip install -r doc/python_api/requirements.txt
```

### Building the Documentation

With the requirements in place, you can go ahead and build the docs:

```console
### From the Blender source root
make doc_py
```

When it's done, point your browser at doc/python_api/sphinx-out/index.html .

### Modifying API Documentation

Because the API docs are produced directly out of Blender's source, things like method signatures and class descriptions originate either in C/C++ files (via PyDoc_STRVAR ) or in plain Python doc-strings.

To revise an API class or method description:

- Track down the source file you need within the Blender repository.

- Find the doc-string you're after: in the Python C/API it sits within PyDoc_STRVAR(...) ,
while in a Python file it's just a regular doc-string.

- Make your edits in reStructuredText.

- Regenerate the pages by rebuilding the Python API docs with make doc_py .

### Adding Example Code Snippets

Examples carry a lot of weight in the API docs. Sitting above the reference for each class, function or module, they show people how the thing is actually used.

### Example File Naming Convention

Rather than inlining code-blocks inside the doc-string, examples can live as standalone script files. Drop a file that follows the naming rules below and it gets pulled in for you.

Such example files belong in doc/python_api/examples/ , where the filename decides what each one attaches to:

- A module is targeted by module.N.py (for instance gpu.0.py ).

- A class is targeted by module.ClassName.N.py (for instance bpy.types.Operator.0.py ).

- A method is targeted by module.ClassName.method.N.py (for instance bpy.types.Operator.invoke.0.py ).

- An attribute is targeted by module.ClassName.attribute.N.py (for instance bpy.types.Scene.frame_start.0.py ).

- A module member is targeted by module.member.N.py (for instance bpy.context.object.0.py ).

Multiple examples are allowed; their sequence is governed by N .

### Example File Structure

It's frequently useful to describe what a particular example is demonstrating. So that you can, the file's leading doc-string is extracted and displayed above the code, with its body rendered as reStructuredText.

Lay out each example file along these lines:

[Related references](INDEX.md).
