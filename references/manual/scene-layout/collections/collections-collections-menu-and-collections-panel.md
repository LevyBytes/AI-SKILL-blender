# Collections: Collections Menu, Collections Panel

### Collections Menu

Reference

Mode :

Object Mode

Menu :

Object ‣ Collection

The Collections menu supplies operations for organizing and managing scene objects. Grouping objects simplifies scene structure, controls visibility, and affects rendering behavior. Single objects may reside in multiple groups simultaneously, permitting complex scene management strategies.

Move to Collection M
Reassigns selected objects to another group. Choose from existing groups, create a new one, or shift to the Scene Collection (the top hierarchy level). Following reassignment, objects exit the former collection unless retained elsewhere.

Link to Collection Shift - M
Appends selected objects to an additional group without removing them from prior groups. Objects may simultaneously belong to numerous groups, facilitating cross-view element management. A new group is also creatable.

Create New Collection Ctrl - G
Produces a new group and enrolls selected object(s) in it. Enter the group name through the Create New Collection Adjust Last Operation panel. This group remains unlinked to the active scene.

Remove from Collection Ctrl - Alt - G
Excludes selected objects from a collection. Multi-collection members receive a choice pop-up with full-removal ability.

Remove from All Collections Shift - Ctrl - Alt - G
Excludes selected objects from all group membership.

Add Selected to Active Objects Collection Shift - Ctrl - G
Enrolls selected objects in group(s) that contain the active object. Alternatively, select "All Collections" to replicate the active object's full membership list.

### Collections

Remove Selected from Active Collection Shift - Alt - G
Removes selected objects from the active object's collections.

Hide Other Collections Ctrl - H
Hides all collections except those selected.

### Collections Panel

Reference

Mode :

Object Mode

Panel :

Object tab ‣ Collections

Collections panel.

All collections an object belongs to are listed in the Object Properties Collections panel.

Add to Collection
Adds the selected object to a collection. A pop-up allows specifying the target collection.

(Add to Collection)
Generates a new collection and adds the selected object to it.

Name
Click in the name field to rename a collection.

(Remove Collection)
Removes the object from the specified collection.

(Collection Specials)
Unlink Collection, Select Objects in Collection, Set Offset from Cursor

X, Y, Z
Applies a spatial offset for instanced collections relative to the original object's position.

See also

Appending or Linking Collections

To import a collection from another blend-file, consult this documentation. In summary: File ‣ Link/Append Link, select a blend-file, then the collection.

Tip

Selecting Collections

Collections may be selected through Select Grouped.

[Related references](INDEX.md).
