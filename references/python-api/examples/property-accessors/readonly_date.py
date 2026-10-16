import bpy

scene = bpy.context.scene

# Read-only string property, returns the current date.
def get_date(self):
    import datetime
    return str(datetime.datetime.now())


bpy.types.Scene.test_date = bpy.props.StringProperty(get=get_date)

# Testing the property:
# scene.test_date = "blah"   # This would fail, property is read-only.
print("test_date:", scene.test_date)

# The above outputs something like:
# test_date: 2018-03-14 11:36:53.158653
