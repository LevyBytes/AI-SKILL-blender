import bpy

scene = bpy.context.scene

# Note: the getter/setter callback must use integer identifiers!
test_items = [
    ("RED", "Red", "", 1),
    ("GREEN", "Green", "", 2),
    ("BLUE", "Blue", "", 3),
    ("YELLOW", "Yellow", "", 4),
]


def get_enum(self):
    import random
    return random.randint(1, 4)


def set_enum(self, value):
    print("setting value", value)


bpy.types.Scene.test_enum = bpy.props.EnumProperty(items=test_items, get=get_enum, set=set_enum)

# Testing the property:
print("test_enum:", scene.test_enum)
scene.test_enum = 'BLUE'
print("test_enum:", scene.test_enum)

# The above outputs something like:
# test_enum: YELLOW
# setting value 3
# test_enum: GREEN
