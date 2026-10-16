# Bmesh chain

Copy this complete directory as a Python package named `bmesh_chain` into a location Blender already searches for scripts. Keep its relative imports intact. In Blender, use `import bmesh_chain` followed by `bmesh_chain.run()`. The run function creates and links the chain geometry in the active collection.

- Open when loading the package or finding its entrypoint: [Package initialization](__init__.py).
- Open when you need link geometry: [link geometry](link_geometry.py).
- Open when you need placement: [placement](placement.py).

[Parent topics](../INDEX.md).
