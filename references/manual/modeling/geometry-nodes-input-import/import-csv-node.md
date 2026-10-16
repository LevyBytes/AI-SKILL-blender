# Import CSV Node

## Import CSV Node

### Import CSV Node

The Import CSV node loads tabular (Comma-Separated Values) files and generates a point cloud. Each row becomes a single point; numeric columns map to point attributes.

The header row (if present) furnishes attribute names. Column types are inferred from the first value: integers yield integer attributes, floats yield float attributes.

Note: Only integer and float columns are imported; other types are skipped.

Useful for embedding external tabular datasets into Geometry Nodes workflows—scientific visualization, data-driven procedural generation, or similar tasks.

### Inputs

Path
File path to the CSV source. Must be structured with one row per point, values delimited by a separator character.

Delimiter
Character separating values within each row (comma, semicolon, tab, etc.).

Tip: Use the Special Characters Node to insert tab characters.

### Outputs

Point Cloud
Output geometry as a point cloud; each CSV row produces one point.

[Related references](INDEX.md).
