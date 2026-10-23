# Best Practice: Avoid Copying Lists, Writing Strings to a File - General Python, Parsing Strings (Import/Exporting), Parsing Numbers, Checking String Start/End

#### Avoid Copying Lists

Handing a list or dictionary to a function and letting it edit the thing in place beats returning a brand-new one, since that way Python skips copying the list in memory.

A function that edits a list in place runs leaner than one that spins up a fresh list. The pattern below is generally slower, so save it for the cases where leaving the original untouched genuinely matters:

```pycon
>>> my_list = some_list_func(my_list)
```

This one is generally quicker, with no reassignment and no duplicated list:

```pycon
>>> some_list_func(vec)
```

Note too that handing over a sliced list copies that list into Python memory:

```pycon
>>> foobar(my_list[:])
```

Where my_list runs to tens of thousands of entries, a copy like that could swallow a good deal of extra memory.

### Writing Strings to a File - General Python

Below are three ways to fuse several strings into one before writing. The same lessons carry over to anywhere your code does heavy string joining:

String concatenation
The slowest of the bunch: steer clear where you can, above all when writing data inside a loop.

```pycon
>>> file.write(str1 + " " + str2 + " " + str3 + "\n")
```

String formatting
Reach for this when you're emitting string data built from floats and ints.

```pycon
>>> file.write("%s %s %s\n" % (str1, str2, str3))
```

String joining
Use this to weld together a list of strings (which can be temporary). In the example below a space " " sits between them; other separators might be "" or ", ".

```pycon
>>> file.write(" ".join((str1, str2, str3, "\n")))
```

For many strings join wins; string formatting is pretty quick too, and better when you're converting data types. Concatenation trails the field.

### Parsing Strings (Import/Exporting)

With so many file formats being ASCII, how you parse and export strings can swing your script's speed considerably.

A few options exist for parsing strings as you bring them into Blender.

#### Parsing Numbers

Prefer float(string) to eval(string) ; and where you know the value is an int, int(string) . float() copes with an int as well, but reading ints through int() is quicker.

#### Checking String Start/End

To test the front of a string for a keyword, rather than:

[Related references](INDEX.md).
