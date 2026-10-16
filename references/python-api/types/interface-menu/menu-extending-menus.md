# bpy.types.Menu: Extending Menus

### Extending Menus

Because add-on menus cannot point at the menus declared in Blender's bundled scripts, the workaround is to attach new entries onto menus that already exist.

Here `menu_draw` behaves the same way `Menu.draw` does.

```python
import bpy

def menu_draw(self, context):
    self.layout.operator("wm.save_homefile")

bpy.types.TOPBAR_MT_file.append(menu_draw)
```

[Related references](INDEX.md).
