# Best Practice: Style Conventions, User Interface Layout

## Best Practice

### Best Practice

Python is an easy language for a beginning developer to get productive in when writing scripts, but along the way it's just as easy to absorb sloppy habits or end up with scripts other people struggle to follow. That's perfectly fine for your private work; once you want to collaborate or get your code bundled with Blender, though, there are conventions we'd recommend.

### Style Conventions

For Blender Python work we've settled on Python's recommended style guide, which keeps our own scripts from drifting into clashing styles and makes pulling in Python from elsewhere smoother. Following the same guide in your scripts pays off if you later decide to contribute them to Blender.

That guide goes by the name pep8,
and what follows is a short rundown of its rules:

- Class names written in camel caps: MyClass

- Module names kept lower case with words joined by underscores: my_module

- Four-space indentation, never tabs

- Operators padded with spaces: 1 + 1 , not 1+1

- Imports always explicit — no wildcard importing *

- One statement per line: instead of if val: body on a single line, break it across two.

On top of pep8 we layer a few extra conventions for Blender Python scripts:

- Wrap enums in single quotes and ordinary strings in double quotes.

Technically both are strings, but in our internal API an enum is a distinct item drawn from a fixed set, e.g:

```python
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = "//render_out"
```

- pep8 additionally caps lines at 79 characters; we've judged that too tight, so we leave it optional on a per-script basis.

### User Interface Layout

A few things worth bearing in mind as you write UI layouts:

The layout code stays straightforward. Layout declarations exist so you can throw together a respectable arrangement with little fuss. The rule of thumb: if your layout declaration needs more code than the properties it's arranging, something's gone wrong.

Example layouts:

layout()
Top-to-bottom stacking is what the plain layout gives you.

```python
layout.prop()
layout.prop()
```

layout.row()
When two or more properties should share a single line, that's the job for row().

```python
row = layout.row()
row.prop()
row.prop()
```

layout.column()
When properties should run down a column, that's the job for column().

```python
col = layout.column()
col.prop()
col.prop()
```

[Related references](INDEX.md).
