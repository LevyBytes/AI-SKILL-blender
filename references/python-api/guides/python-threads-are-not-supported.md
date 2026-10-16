# Python Threads are Not Supported

## Python Threads are Not Supported

### Python Threads are Not Supported

The short version: Python threads make Blender crash in ways that are hard to diagnose. A crash might surface while Cycles is rendering, while Python drivers run, or while a background thread is busy fetching some file.

Thread safety for the way Python is wired into Blender has had no work done on it so far, and until that's properly sorted out the safest course is to steer clear of threads entirely.

Bear in mind, too, that parts of the standard library rely on threads internally — the multiprocessing.Queue class being a case in point.

Python threading works correctly with Blender only when the threads wrap up before the script does — for instance by calling threading.Thread.join() . Put differently, they're usable only while the main Blender thread is held from running.

### Alternative Approaches

To run Python code independently of Blender, the recommended tool is the multiprocessing module.

### Code Examples

Here's a threading example that Blender supports:

```python
import threading
import requests

urls = [
   "http://localhost:8000/file-1.blend",
   "http://localhost:8000/file-2.blend",
   "http://localhost:8000/file-3.blend",
]


def download(url: str) -> None:
   name = threading.current_thread().name
   print("{}: Starting".format(name))
   response = requests.get(url)
   print("{}: Request status code {}".format(name, response.status_code))


threads = [
   threading.Thread(
      name="thread-{}".format(index),
      target=download,
      args=(url,),
   )
   for index, url in enumerate(urls)
]

print("Starting threads...")
for t in threads:
   t.start()

# NOTE: While threads are running, no code (including the main thread)
# may use bpy or any Blender API - only standard Python or third-party modules.
print("Waiting for threads to finish...")
for t in threads:
   t.join()

# It's now safe to use bpy again since all threads have finished.
print("Threads all done, now Blender can continue")
```

And here's a case that isn't supported, a timer that fires many times each second:

```python
from threading import Timer

def my_timer():
      t = Timer(0.1, my_timer)
      t.daemon = True
      t.start()
      print("Running...")

my_timer()
```

Patterns like that one, which leave a thread alive after the script ends, may appear to hold up for a while, but they wind up triggering random crashes or errors inside Blender's own drawing code.

[Related references](INDEX.md).
