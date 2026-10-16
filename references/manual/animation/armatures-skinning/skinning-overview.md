# Introduction

Having designed an armature and built bone chains, a good rig isn't the end goal — unless you're making a "Danse Macabre," you'll want to put flesh on the skeleton, and "linking" an armature to the object(s) it should transform or deform is, fittingly, called skinning. Blender has two main skinning types: Parent/Constrain Objects to Bones — transforming the bones in Pose Mode then transforms their "children" objects exactly like a normal parent/child relationship, and the children are never deformed; or Use the Armature Modifier on an entire mesh, tying parts of the object to bones inside the armature — the more complex and powerful method, and the only one that truly deforms the geometry by changing its vertices' relative positions. Retargeting — applying real-world motion-capture data to a rig — is available through add-ons and importers.

[Related references](INDEX.md).
