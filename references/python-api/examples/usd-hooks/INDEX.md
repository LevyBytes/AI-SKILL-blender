# Usd hooks

Copy this complete directory as a Python package named `usd_hooks` into a location Blender already searches for scripts. Keep its relative imports intact. In Blender, use `import usd_hooks` followed by `usd_hooks.register()`. Use `usd_hooks.unregister()` to remove the registered example. The entrypoint exposes Blender's bundled modules before importing the USD helpers.

- Open when loading the package or finding its entrypoint: [Package initialization](__init__.py).
- Open when you need exports: [exports](exports.py).
- Open when you need material import: [material import](material_import.py).
- Open when you need stage import: [stage import](stage_import.py).

[Parent topics](../INDEX.md).
