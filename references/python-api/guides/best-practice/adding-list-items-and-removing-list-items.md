# Best Practice: Adding List Items, Removing List Items

```python
polygons = [p for p in mesh.polygons if len(p.vertices) != 3]
```

#### Adding List Items

When you've got one list to merge into another, instead of:

```python
for l in some_list:
    my_list.append(l)
```

Use:

```python
my_list.extend([a, b, c])
```

Keep in mind insert is there for when you need it, yet it lags append, particularly when you insert near the front of a long list. The snippet below is a thoroughly inefficient way to build a reversed list:

```python
reverse_list = []
for list_item in some_list:
    reverse_list.insert(0, list_item)
```

Python offers tidier ways to reverse a list via slicing, though it's worth timing before you lean on it heavily:

```python
some_reversed_list = some_list[::-1]
```

#### Removing List Items

Prefer my_list.pop(index) over my_list.remove(list_item) . That does mean having the item's index on hand, but it's quicker since remove() has to search the list. Here's how to clear items inside a single loop, taking the last ones first, which (as noted above) is faster:

```python
list_index = len(my_list)

while list_index:
    list_index -= 1
    if my_list[list_index].some_test_attribute == 1:
        my_list.pop(list_index)
```

The next snippet is a fast removal trick, suitable wherever you can shuffle the list order without breaking what the script does. It swaps two entries so the one you're dropping always ends up last:

```python
pop_index = 5

### Swap so the pop_index is last.
my_list[-1], my_list[pop_index] = my_list[pop_index], my_list[-1]

### Remove last item (pop_index).
my_list.pop()
```

Across a big list with many items to clear, this can buy you a solid speed-up.

[Related references](INDEX.md).
