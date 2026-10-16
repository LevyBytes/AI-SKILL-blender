# Extrude Mesh Node: Edge Mode, Face Mode, Individual Face Mode

### Edge Mode

Vertical connecting edges (shown in yellow) average from the two middle blue edges; darker maroon edges below are unused.

- New vertices copy from originals.

- Vertical connecting edges average from any connected extruded edges. Booleans: selected if any were selected. (Propagation shown in figure.)

- Horizontal duplicate edges copy from originals.

- New faces average from all faces adjacent to selected edges. Booleans: selected if any were.

- New face corners average from corresponding corners in all adjacent faces. Booleans: selected if one was.

### Face Mode

Vertical connecting edges (shown in yellow) average from the two middle blue edges; darker maroon edges between unselected/top faces are unused.

- New vertices copy from originals.

- Vertical connecting edges average from any connected extruded edges, excluding "top" edges. Booleans: selected if any were. (Propagation shown in figure.)

- Horizontal duplicate edges copy from originals.

- New faces copy from corresponding extruded faces.

- New face corners copy from corresponding extruded-face corners.

### Individual Face Mode

Each edge averages from its two neighbors on the extruded face.

- New vertices copy from originals.

- Vertical connecting edges average from the two neighbors on each extruded face. Booleans: selected when at least one neighbor was.

- Horizontal duplicate edges copy from originals.

- New side faces copy from their corresponding selected face.

- New face corners copy from their corresponding selected-face corners.

[Related references](INDEX.md).
