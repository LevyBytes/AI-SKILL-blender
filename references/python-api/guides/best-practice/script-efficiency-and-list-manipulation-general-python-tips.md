# Best Practice: Script Efficiency, List Manipulation (General Python Tips), Searching for List Items, Modifying Lists

layout.split()
This is your tool for richer arrangements — for instance, splitting the layout to sit two column() layouts next to one another. Putting two properties on one line isn't a reason to split; row() handles that.

```python
split = layout.split()

col = split.column()
col.prop()
col.prop()

col = split.column()
col.prop()
col.prop()
```

Declaration names:

When you declare layouts, try to keep to this set of variable names:

row :

names a row() layout

col :

names a column() layout

split :

names a split() layout

flow :

names a column_flow() layout

sub :

names a nested layout (such as a column placed inside another column)

### Script Efficiency

### List Manipulation (General Python Tips)

#### Searching for List Items

Python ships a few convenient list functions that spare you from scanning the list by hand. Even though you aren't writing the loop yourself, Python still is — so stay mindful of calls that drag your script down by walking the whole list.

```python
my_list.count(list_item)
my_list.index(list_item)
my_list.remove(list_item)
if list_item in my_list: ...
```

#### Modifying Lists

Adding to or removing from a Python list gets slower once the list's length changes, and worse near the front, because every element past the edit point has to shift one slot up or down.

For appending at the end, your fastest options are my_list.append(list_item) or my_list.extend(some_list) ; to discard the final element, reach for my_list.pop() or del my_list[-1] .

If you instead need to work by index, my_list.insert(index, list_item) adds and list.pop(index) removes — but expect both to run more slowly.

At times it's quicker — though heavier on memory — to simply rebuild the list outright. Take stripping every triangular polygon from a list. Rather than:

```python
polygons = mesh.polygons[:]  # Make a list copy of the meshes polygons.
p_idx = len(polygons)        # Loop backwards
while p_idx:                 # While the value is not 0.
    p_idx -= 1

    if len(polygons[p_idx].vertices) == 3:
        polygons.pop(p_idx)  # Remove the triangle.
```

A list comprehension builds the new list faster:

[Related references](INDEX.md).
