# File Paths

## File Paths

Path Templates: path templates swap template expressions (written {abcd}, where "abcd" is a variable name) into a filepath when the path is used. For example, say the open blend file is dance.blend and your render output path reads:
```text
//my_render_dir/{blend_name}.png
```
then at render time Blender treats the path as:
```text
//my_render_dir/dance.png
```
with {blend_name} replaced by dance from dance.blend. The substitution happens internally at the moment of use (while rendering, say), so the template syntax stays as-is in the path field. Note: for now, templates apply only to the render output path under Scene properties and to the output paths on the compositor's File Output node; more filepaths will gain template support in future releases.

Available Variables: these are currently available in template expressions.
Available in every path that supports templates:
blend_name: the open blend file's name (minus the .blend).
blend_dir: the path up to (but not including) the open blend file.
blend_name_lib: like blend_name, except that on path properties of library-linked data-blocks it's the name of the library blend file the data-block comes from.
blend_dir_lib: like blend_dir, except that on path properties of library-linked data-blocks it's the path to the library blend file the data-block comes from.
Available only in render output paths (the compositor File Output node included):
fps: the current scene's frames per second.
resolution_x / resolution_y: the rendered image's x and y resolution; this folds in the resolution scale, so a 1000x600 scene at 50% scale gives resolution_x and resolution_y of 500 and 300.
scene_name: the current scene's name.
camera_name: the current render camera's name.
Found only on a node's path properties:
node_name: the name of the node carrying the path property.

Syntax: a basic template expression just wraps a variable name in curly braces:
```text
dance_{fps}.png
```
Format Specifiers: a template expression can also carry a format specifier telling Blender how to format the substituted value; it follows a separating colon:
```text
dance_{fps:FORMAT}.png
```
Format specifiers currently work only with variables that hold numbers, not strings. The available ones:
- dance_{fps:###}.png — formats as an integer with at least 3 digits.
- dance_{fps:.###}.png — formats as a float with exactly 3 digits after the decimal point.
- dance_{fps:###.##}.png — formats as a float with at least 3 integer digits and exactly 2 fractional digits.
In every case the count of hash symbols (#) sets how many digits you want. For instance, with fps of 29.97:
- dance_{fps:###}.png -> dance_030.png
- dance_{fps:.###}.png -> dance_29.970.png
- dance_{fps:###.##}.png -> -> dance_029.97.png
Note that values are properly rounded for the chosen digit count. With no format spec, the variable's default formatting applies (float for fps, integer for resolution).

Escape Sequences: because { and } drive template expressions in paths that support them, a literal { or } in such a path must be doubled:
- {{ becomes a single { in the final path.
- }} becomes a single } in the final path.
For example:
- my_weird}}_{{path.png -> my_weird}_{path.png
- //my_render_{{dir}}/{blend_name}.png -> //my_render_{dir}/dance.png
- //my_render_dir/{{{blend_name}}}.png -> //my_render_dir/{dance}.png

Errors: paths that support templates can hold template errors that block processing. In this path, for example:
```text
//my_render_dir/{blend_name.png
```
the expression {blend_name isn't closed properly, which errors. When a path has template errors, its field is highlighted red in the UI, and hovering it pops a tooltip listing the errors found. Note: depending on the path, template errors may block certain actions — errors in the render output path, for instance, make rendering an animation fail with a message about the path errors.

[Related references](INDEX.md).
