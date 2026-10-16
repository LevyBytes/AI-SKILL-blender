# Custom render engine

Copy this complete directory as a Python package named `custom_render_engine` into a location Blender already searches for scripts. Keep its relative imports intact. In Blender, use `import custom_render_engine` followed by `custom_render_engine.register()`. Use `custom_render_engine.unregister()` to remove the registered example.

- Open when loading the package or finding its entrypoint: [Package initialization](__init__.py).
- Open when you need draw data: [draw data](draw_data.py).
- Open when you need engine: [engine](engine.py).
- Open when you need render pixels: [render pixels](render_pixels.py).
- Open when you need viewport drawing: [viewport drawing](viewport_drawing.py).
- Open when you need viewport updates: [viewport updates](viewport_updates.py).

[Parent topics](../INDEX.md).
