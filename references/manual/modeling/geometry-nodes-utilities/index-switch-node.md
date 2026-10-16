# Index Switch Node

## Index Switch Node

The Index Switch node outputs one of its inputs by an integer Index, evaluating only the selected input — efficient for switching between several data inputs. (The Menu Switch node is similar but exposes the choice as a menu rather than an index.) Inputs: Index (which input socket passes through, zero-based so the first input is index 0) plus one socket per possible input, with more added by dragging a connection onto the bottom empty socket or clicking the header icon — and a tip notes that when Index connects to a Menu Switch set to Integer Type, the matching menu labels show next to the index for readability. Properties: Type (the data type the node handles). Output: Output (the value from the input at the current Index, unmodified, or, if Index is out of range, the first input or a zero-equivalent value by type).

### Index Switch Node

Pass through one input based on an integer Index.
Only the selected input evaluates, enabling efficient switching.

**See also:** Menu Switch offers a user-friendly menu instead of index.

### Inputs

**Index**
Selects which input to pass (zero-based; first = 0).

Each socket is a possible selection.
Active input: determined by Index.

Add sockets by:
- Dragging to the empty bottom socket.
- Clicking the header icon.

**Tip:** Connect Index to Menu Switch set to Integer Type—menu labels appear next to the index, clarifying meanings and improving readability.

### Properties

**Type**
Data type handled.

### Outputs

**Output**
Value from the selected input, unmodified.
Index out of range: defaults to first input or zero-equivalent.

[Related references](INDEX.md).
