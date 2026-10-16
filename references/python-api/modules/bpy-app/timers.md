# bpy.app.timers

## Application Timers (bpy.app.timers)

### Application Timers (bpy.app.timers)

### Run a Function in x Seconds
```python
import bpy

def in_5_seconds():
    print("Hello World")

bpy.app.timers.register(in_5_seconds, first_interval=5)
```

### Run a Function every x Seconds
```python
import bpy

def every_2_seconds():
    print("Hello World")
    return 2.0

bpy.app.timers.register(every_2_seconds)
```

### Run a Function n times every x seconds
```python
import bpy

counter = 0

def run_10_times():
    global counter
    counter += 1
    print(counter)
    if counter == 10:
        return None
    return 0.1

bpy.app.timers.register(run_10_times)
```

### Assign parameters to functions
```python
import bpy
import functools

def print_message(message):
    print("Message:", message)

bpy.app.timers.register(functools.partial(print_message, "Hello"), first_interval=2.0)
bpy.app.timers.register(functools.partial(print_message, "World"), first_interval=3.0)
```
bpy.app.timers. is_registered ( function )
Checks whether this function is registered as a timer.
Parameters: function ( Callable [ [ ] , float | None ] ) – Function to check.
Returns: True when this function is registered, otherwise False.
Return type: bool
bpy.app.timers. register ( function , * , first_interval = 0 , persistent = False )
Adds a new function to be called after the given number of seconds. The function takes no arguments and should return either None or a float: returning None unregisters the timer, while a returned number sets the delay until it's called again. functools.partial can be used to assign some parameters.
Parameters:
- function ( Callable [ [ ] , float | None ] ) – The function that should called.
- first_interval ( float ) – Seconds until the callback should be called the first time.
- persistent ( bool ) – Don't remove timer when a new file is loaded.
bpy.app.timers. unregister ( function )
Unregisters a timer.
Parameters: function ( Callable [ [ ] , float | None ] ) – Function to unregister.

[Related references](INDEX.md).
