# Tips And Tricks: Insert a Python Interpreter into your Script, Advanced, Blender as a Module, Python Safety (Build Option)

```console
PYTHONPATH=/usr/lib/python3.7 ./blender --python-use-system-env
```

Warning

The Python (major, minor) version has to line up with the one Blender ships with. So Python 3.6 won't work against a Blender built for Python 3.7.

- Copy or symlink the extensions into Blender's Python subdirectory so Blender picks them up; you can even drop the whole Python installation into Blender's subdirectory, swapping out the one it came with. That holds up as long as the Python versions agree and the paths land in matching relative spots. The payoff is that you can then hand this bundle, Blender plus whatever extensions you depend on, off to others.

### Insert a Python Interpreter into your Script

Partway through a script you might want to peek at variables, call functions, and trace the flow.

```python
import code
code.interact(local=locals())
```

To reach both global and local variables, run this:

```python
import code
namespace = globals().copy()
namespace.update(locals())
code.interact(local=namespace)
```

This next one is a one-line equivalent of the snippet above, which makes it simpler to drop into your code:

```text
__import__('code').interact(local=dict(globals(), **locals()))
```

You can stick code.interact on any line of the script; it halts execution and opens an interactive interpreter in the terminal, and once you're finished you quit the interpreter and the script picks up where it left off.

Should you have IPython installed, its embed() function works too and inherits the current namespace. The IPython prompt brings auto-complete and a few niceties that the stock Python eval-loop lacks.

```python
import IPython
IPython.embed()
```

Granted, this rather underscores that Blender ships without any built-in Python debugging support, but it's still a useful thing to have in your back pocket.

### Advanced

### Blender as a Module

From a Python standpoint it's tidier to treat the whole thing as an extension, letting a Python script stitch together many pieces.

Among the benefits:

- Outside editors and IDEs can be wired up against the Python API of Blender, with scripts run straight from within the IDE (stepping through code, watching variables as it goes).

- Editors and IDEs can offer auto-complete for Blender's modules and variables.

- Scripts you already have can import Blender's APIs without needing to run inside Blender.

This carries the advanced label because running Blender as a Python module calls for a special build option. For build instructions, see Building Blender as a Python module.

### Python Safety (Build Option)

Since it's possible to reach data that has already been freed (see Gotchas), chasing down what caused a crash can be tough. To have Python throw exceptions when freed data is accessed, rather than crashing outright, switch on the CMake build option `WITH_PYTHON_SAFETY`. Doing so turns on data tracking, which roughly halves data-access speed, which is exactly why release builds leave it off.

[Related references](INDEX.md).
