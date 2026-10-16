import bpy

scene = bpy.context.scene

# Boolean array, using 'transform' accessors.
# Note how the same result is achieved as with previous get/set example, but using default RNA storage.
# Transform accessors also have access to more information.
# Also note how the stored data _is_ a two-items array.
# - Set function stores a single boolean value, returned as the second component.
# - Array getters must return a list or tuple.
# - Array size must match the property vector size exactly.
def get_array_transform(self, curr_value, is_set):
    print("Stored data:", curr_value, "(is set:", is_set, ")")
    return (True, curr_value[1])


def set_array_transform(self, new_value, curr_value, is_set):
    print("New data:", new_value, "; Stored data:", curr_value, "(is set:", is_set, ")")
    return True, new_value[0] and new_value[1]


bpy.types.Scene.test_array_transform = bpy.props.BoolVectorProperty(
    size=2, get_transform=get_array_transform, set_transform=set_array_transform)

# Testing the property:
print("test_array_transform:", tuple(scene.test_array_transform))
scene.test_array_transform = (True, False)
print("test_array_transform:", tuple(scene.test_array_transform))

# The above outputs:
# Stored data: (False, False) (is set: False )
# test_array_transform: (True, False)
# New data: (True, False) ; Stored data: (False, False) (is set: False )
# Stored data: (True, False) (is set: True )
# test_array_transform: (True, False)
