# Index Node

## Index Node

### Index Node

Returns an integer position for each element in the geometry list, starting at zero. Actual order depends on internal topology logic, visible in the Spreadsheet Editor's leftmost column.

**Inputs**
None.

**Outputs**
- Index: Element position.

Caution: Indices follow internal algorithm ordering and may not be predictable when inputs change. They may also vary across Blender versions as algorithms are updated. For stable references, compute indices locally or avoid topology-changing operations when consistency over time is critical.

[Related references](INDEX.md).
