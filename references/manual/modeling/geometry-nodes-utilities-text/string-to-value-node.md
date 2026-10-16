# String to Value Node

## String to Value Node

Parses a text string into a numeric value.
Useful for converting text from user input, files, or dynamic sources into numbers.

The node reads characters from the start until a number is successfully parsed.
Parsing failure returns 0.0.

**Inputs**

String
The input text to convert.

**Properties**

Data Type

Float: Parse as floating-point.

Integer: Parse as 32-bit integer.

**Outputs**

Value
The converted number.

Length
Character count successfully parsed as part of the number.
Indicates where the numeric portion ends, enabling further substring work.

**Examples**

- `"3.1415"` with Float selected: outputs 3.1415 and length 6.

- `"42abc"` with Integer selected: outputs 42 and length 2.

- `"hello"`: outputs 0 and length 0.

[Related references](INDEX.md).
