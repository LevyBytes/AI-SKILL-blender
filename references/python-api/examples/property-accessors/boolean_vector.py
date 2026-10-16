import bpy

scene = bpy.context.scene

# Boolean array.
# - Set function stores a single boolean value, returned as the second component.
# - Array getters must return a list or tuple.
# - Array size must match the property vector size exactly.
def get_array(self):
    return (True, self.get("somebool", True))


def set_array(self, values):
    self["somebool"] = values[0] and values[1]


bpy.types.Scene.test_array = bpy.props.BoolVectorProperty(size=2, get=get_array, set=set_array)

# Testing the property:
print("test_array:", tuple(scene.test_array))
scene.test_array = (True, False)
print("test_array:", tuple(scene.test_array))

# The above outputs:
# test_array: (True, True)
# test_array: (True, False)
