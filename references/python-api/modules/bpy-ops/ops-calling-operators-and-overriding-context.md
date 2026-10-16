# bpy.ops: calling operators and overriding context

## Operators (bpy.ops)

Python Operator Framework

Describes how to invoke bpy.ops functions with context overrides and execution modes

The bpy.ops interface grants Python-based access to operator functions written in C++, Python, or macro recipes. It accepts only named parameter keywords.

Operators do not yield conventional return codes; instead they yield a collection containing one or more elements from:
{'`RUNNING_MODAL`', 'CANCELLED', 'FINISHED', '`PASS_THROUGH`'}.
Standard outcomes are {'FINISHED'} and {'CANCELLED'} (termination without state change or undo history).

If an operator is cancelled without error reports of type {'ERROR'}, it returns {'CANCELLED'} without exception.
When error messages exist, a RuntimeError fires post-execution with all error content, regardless of completion status.

Invoking an operator in an incompatible context raises RuntimeError. The poll() method allows context verification beforehand.

The identifier in the example (mesh.subdivide) is the bl_idname; bpy.ops provides the Python path.

Keyword and Positional Argument Syntax

Operators use keyword arguments for properties and positional arguments for call modifiers.

Two modifiers are supported (in strict order):

```text
bpy.ops.test.operator(execution_context, undo)
```

- execution_context - enum (str type).
- undo - bool

Both are optional but must appear in this sequence.

```python
import bpy

# Calling an operator.
bpy.ops.mesh.subdivide(number_cuts=3, smoothness=0.5)


# Check poll() to avoid exception.
if bpy.ops.object.mode_set.poll():
    bpy.ops.object.mode_set(mode='EDIT')
```

Context Substitution

It is possible to override context bindings that an operator perceives, allowing operation on specified rather than selected or active data, or to execute within a different UI region.

The context replacements are supplied as keyword arguments whose names match bpy.context members.
For instance, to replace bpy.context.active_object, you supply active_object=object to bpy.types.Context.temp_override.

Note: a duplicate of the live context is nearly always preferable as a baseline (else, you must gather all dependencies yourself).

Note: context member names are the data-access names used in Blender; overrides do not extend to Python-specific methods or functions.

```python
# Remove all objects in scene rather than the selected ones.
import bpy
from bpy import context
context_override = context.copy()
context_override["selected_objects"] = list(context.scene.objects)
with context.temp_override(**context_override):
    bpy.ops.object.delete()
```

[Related references](INDEX.md).
