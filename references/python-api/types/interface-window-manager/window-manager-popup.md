# bpy.types.WindowManager: popup_menu, popup_menu_pie

popup_menu ( draw_func , * , title = '' , icon = 'NONE' )

Popup menus offer a way to build menus without registering menu classes first.

Because such a menu does not halt the running script, the caller has no way to pause for user input.

```python
import bpy


def draw(self, context):
    self.layout.label(text="Hello World")


bpy.context.window_manager.popup_menu(draw, title="Greeting", icon='INFO')
```
popup_menu_pie ( event , draw_func , * , title = '' , icon = 'NONE' )

[Related references](INDEX.md).
