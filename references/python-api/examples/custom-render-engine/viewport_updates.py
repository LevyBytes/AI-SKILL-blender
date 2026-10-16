# For viewport renders, this method gets called once at the start and
# whenever the scene or 3D viewport changes. This method is where data
# should be read from Blender in the same thread. Typically a render
# thread will be started to do the work while keeping Blender responsive.
def view_update(self, context, depsgraph):
    region = context.region
    view3d = context.space_data
    scene = depsgraph.scene

    # Get viewport dimensions
    dimensions = region.width, region.height

    if self.scene_data is None:
        # First time initialization
        self.scene_data = []
        first_time = True

        # Loop over all datablocks used in the scene.
        for datablock in depsgraph.ids:
            pass
    else:
        first_time = False

        # Test which datablocks changed
        for update in depsgraph.updates:
            print("Datablock updated: ", update.id.name)

        # Test if any material was added, removed or changed.
        if depsgraph.id_type_updated('MATERIAL'):
            print("Materials updated")

    # Loop over all object instances in the scene.
    if first_time or depsgraph.id_type_updated('OBJECT'):
        for instance in depsgraph.object_instances:
            pass
