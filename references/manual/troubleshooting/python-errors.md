# Python Errors

## Python Errors

### Python Errors

### Precompiled Libraries

Though uncommon, Python add-ons sometimes bundle their own compiled libraries. These differ from plain Python code—they do not transfer between operating systems.

A precompiled library might not work with your Blender setup (perhaps it was compiled for a different Python version, or you are trying to load 32-bit code on a 64-bit system).

Check that any included .pyd or .so files match your OS.

### Platform Specific

### Windows

#### Mixed Python Libraries (DLLs)

Python errors or add-on failures during activation (e.g: ... is not a valid Win32 application.) often trace back to conflicting system libraries. Although Blender ships with its own Python, duplicate or incompatible copies can interfere.

A Python traceback.

To identify which library is causing failure, check the error output.

This usually appears near the end of the traceback. The example above pinpoints _socket. This corresponds to a file named _socket.py or _socket.pyd.

You can paste this script into the Text editor and run it to search for conflicting copies of your library.
(Output appears in the Command Line Window.)

```python
import os
import sys

# Change this based on the library you wish to test
test_lib = "_socket.pyd"

def GetSystemDirectory():
    from ctypes import windll, create_string_buffer, sizeof
    GetSystemDirectory = windll.kernel32.GetSystemDirectoryA
    buffer = create_string_buffer(260)
    GetSystemDirectory(buffer, sizeof(buffer))
    return os.fsdecode(buffer.value)

def library_search_paths():
    return (
        # Windows search paths
        os.path.dirname(sys.argv[0]),
        os.getcwd(),
        GetSystemDirectory(),
        os.environ["WINDIR"],  # GetWindowsDirectory
        *os.environ["PATH"].split(";"),

        # regular Python search paths
        *sys.path,
        )

def check_library_duplicate(libname):
    paths = [p for p in library_search_paths()
             if os.path.exists(os.path.join(p, libname))]

    print("Library %r found in %d locations:" % (libname, len(paths)))
    for p in paths:
        print("- %r" % p)

check_library_duplicate(test_lib)
```

[Related references](INDEX.md).
