# Format String Node: Format Items, Input Naming Behavior, Basic, Multiple Values

## Format String Node

Inserts values into a string using Python-compatible or Blender format syntax.

Simplifies string assembly by formatting values inline without manual string conversion or stacked concatenation nodes.

See also: Python Format String Syntax and {fmt} Format String Syntax.

**Inputs**

Format
A string with placeholders: `Count: {}` inserts the first value; `Count: {name}` inserts a named parameter.

Additional numeric or text inputs are managed via the Format Items list in the sidebar.

**Properties**

### Format Items

List view for adding, removing, reordering, and renaming dynamic inputs.
Each entry corresponds to an insertable value.

Socket Type

Float: Floating-point number (e.g., 3.14).

Integer: Integer number (e.g., 42).

String: Text string.

**Outputs**

String
The assembled string.

**Notes**

- Supports both unnamed (`{}`) and named (`{name}`) placeholders; all unnamed must precede named.

- Supports float, integer, and string inputs only.

- Python conversions like `!r` are unsupported.

- Sub-attribute access (e.g., `{vector.x}`) is unsupported.

- Percent-style formatting (e.g., `%d`) is unsupported.

- Alternate forms using `#` (e.g., `{:#x}`) are unsupported.

- Locale formatting via `L` is unsupported.

- Grouping separators (e.g., `{:,}`, `{:_}`) are unsupported.

### Input Naming Behavior

Each input needs a unique, valid identifier for placeholders (e.g., `{value}`).
Auto-naming logic:

- If connected, uses the first character of the linked socket name.

- Otherwise defaults to letters a–z.

- Converts invalid names to valid identifiers.

- Appends a suffix (e.g., `_001`) as a fallback.

Important: Names must be valid identifiers and unique. Invalid names may cause formatting errors.

**Examples**

### Basic

Format: `Count: {}`
Inputs: Integer 5
Result: `Count: 5`

### Multiple Values

Format: `X: {}, Y: {}`
Inputs: Float 1.5, Float 2.0
Result: `X: 1.5, Y: 2.0`

[Related references](INDEX.md).
