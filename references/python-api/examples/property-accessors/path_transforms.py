import bpy

scene = bpy.context.scene

# String, using 'transform' accessors to validate data before setting/returning it.
def get_string_transform(self, curr_value, is_set):
    import os
    is_valid_path = os.path.exists(curr_value)
    print("Stored data:", curr_value, "(is set:", is_set, ", is valid path:", is_valid_path, ")")
    return curr_value if is_valid_path else ""


def set_string_transform(self, new_value, curr_value, is_set):
    import os
    is_valid_path = os.path.exists(new_value)
    print("New data:", new_value, "(is_valid_path:", is_valid_path, ");",
          "Stored data:", curr_value, "(is set:", is_set, ")")
    return new_value if is_valid_path else curr_value


bpy.types.Scene.test_string_transform = bpy.props.StringProperty(
    subtype='DIR_PATH',
    default="an/invalid/path",
    get_transform=get_string_transform,
    set_transform=set_string_transform,
)

# Testing the property:
print("test_string_transform:", scene.test_string_transform)
scene.test_string_transform = "try\\to\\find\\me"
print("test_string_transform:", scene.test_string_transform)

# The above outputs something like:
# Stored data: an/invalid/path (is set: False , is valid path: False )
# test_string_transform:
# New data: try\to\find\me (is_valid_path: False ) ; Stored data: an/invalid/path (is set: False )
# Stored data: an/invalid/path (is set: True , is valid path: False )
# test_string_transform:
