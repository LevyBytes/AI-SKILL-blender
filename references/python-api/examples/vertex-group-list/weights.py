def filter_items_empty_vgroups(self, context, vgroups):
    # This helper function checks vgroups to find out whether they are empty, and what's their average weights.
    # TODO: This should be RNA helper actually (a vgroup prop like `"raw_data: ((vidx, vweight), etc.)"`).
    #       Too slow for Python!
    obj_data = context.active_object.data
    ret = {vg.index: [True, 0.0] for vg in vgroups}
    if hasattr(obj_data, "vertices"):  # Mesh data
        if obj_data.is_editmode:
            import bmesh
            bm = bmesh.from_edit_mesh(obj_data)
            # only ever one deform weight layer
            dvert_lay = bm.verts.layers.deform.active
            fact = 1 / max(1, len(bm.verts))
            if dvert_lay:
                for v in bm.verts:
                    for vg_idx, vg_weight in v[dvert_lay].items():
                        ret[vg_idx][0] = False
                        ret[vg_idx][1] += vg_weight * fact
        else:
            fact = 1 / max(1, len(obj_data.vertices))
            for v in obj_data.vertices:
                for vg in v.groups:
                    ret[vg.group][0] = False
                    ret[vg.group][1] += vg.weight * fact
    elif hasattr(obj_data, "points"):  # Lattice data
        # XXX: no access to lattice edit-data?
        fact = 1 / max(1, len(obj_data.points))
        for v in obj_data.points:
            for vg in v.groups:
                ret[vg.group][0] = False
                ret[vg.group][1] += vg.weight * fact
    return ret
