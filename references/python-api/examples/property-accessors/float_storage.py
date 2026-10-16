import bpy

scene = bpy.context.scene

# Simple property reading/writing from 'custom' IDProperties.
# This is similar to what the RNA would do internally, albeit using it own separate,
# internal 'system' IDProperty storage, since Blender 5.0.
def get_float(self):
    return self.get("testprop", 0.0)


def set_float(self, value):
    self["testprop"] = value


bpy.types.Scene.test_float = bpy.props.FloatProperty(get=get_float, set=set_float)

# Testing the property:
print("test_float:", scene.test_float)
scene.test_float = 7.5
print("test_float:", scene.test_float)

# The above outputs:
# test_float: 0.0
