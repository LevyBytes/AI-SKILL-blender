# Building the Manual

## Building the Manual

Converting the RST files into HTML pages is simple: open a terminal or Command Prompt in the ~/blender-manual directory and run:
```console
make
```
(On Windows you can just open make.bat to run the command without typing it in the Command Prompt.) This is the command to use when building the docs — other commands are listed by `make help` — and it converts the RST files to HTML, opens your default browser to the result, then keeps running to watch for RST changes and refresh the HTML as needed. The built pages can also be browsed manually under ~/blender-manual/build/html (e.g. open build/html/index.html for the home page). The first build (or after major changes) may take several minutes, but later changes take only a few seconds.

[Related references](INDEX.md).
