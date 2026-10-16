# Best Practice: Error Handling, Value Comparison, Time Your Code

```pycon
>>> if line[0:5] == "vert ": ...
```

Use:

```python
if line.startswith("vert "):
    ...  # Handle the matching line here.
```

startswith() runs a touch faster (roughly 5%) and sidesteps a possible bug where the slice length doesn't line up with the string length.

my_string.endswith("foo_bar") works the same way for line endings.

When you can't be sure of the casing, fold it first with the lower() or upper() string method:

```python
if line.lower().startswith("vert "):
    ...  # Handle the matching line here.
```

### Error Handling

A try statement is a handy shortcut around writing your own error checks. The catch is that try costs noticeably more than an if, since an exception has to be armed each pass, so keep try out of code that loops and runs heavily.

That said, there are situations where try beats testing up front whether something will error, so it's worth experimenting.

### Value Comparison

Python gives you two value comparisons, a == b and a is b . The distinction: == may invoke the object's own __eq__() method, whereas is tests identity — whether both names point at the very same object in memory.

When you already know you're comparing one shared value that's referenced from several places, is comes out faster.

### Time Your Code

As you build a script it's handy to time it so you catch any shift in performance, and that's easy to do:

```python
import time
time_start = time.time()

### Do something...

print("My Script Finished: %.4f sec" % (time.time() - time_start))
```

[Related references](INDEX.md).
