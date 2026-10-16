import bpy
import bmesh
import math
import mathutils

def duplicate_and_place(bm):
    # Now we have made a links of the chain, make a copy and rotate it
    # (so this looks something like a chain)

    ret = bmesh.ops.duplicate(
        bm,
        geom=bm.verts[:] + bm.edges[:] + bm.faces[:])
    geom_dupe = ret["geom"]
    verts_dupe = [ele for ele in geom_dupe if isinstance(ele, bmesh.types.BMVert)]
    del ret

    # position the new link
    bmesh.ops.translate(
        bm,
        verts=verts_dupe,
        vec=(0.0, 0.0, 2.0))
    bmesh.ops.rotate(
        bm,
        verts=verts_dupe,
        cent=(0.0, 1.0, 0.0),
        matrix=mathutils.Matrix.Rotation(math.radians(90.0), 3, 'Z'))

    # Done with creating the mesh, simply link it into the scene so we can see it

    # Finish up, write the bmesh into a new mesh
    me = bpy.data.meshes.new("Mesh")
    bm.to_mesh(me)
    bm.free()


    # Add the mesh to the scene
    obj = bpy.data.objects.new("Object", me)
    bpy.context.collection.objects.link(obj)

    # Select and make active
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    return obj
