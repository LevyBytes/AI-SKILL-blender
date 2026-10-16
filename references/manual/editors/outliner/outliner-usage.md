# Usage

## Usage

Relations Management — objects and collections can be reorganized, linked, or parented right in the Outliner by drag-and-drop — a natural way to handle scene hierarchies and the relationships between them.
Moving and Linking:
  Move — drop one object or collection onto a different collection to relocate it there.
  Link — hold Ctrl while dragging an object (or collection) onto a collection to link rather than move it, letting the same object or collection belong to several parent collections at once.
Parenting:
  Parent to Object — drop one object onto another to make the first a child of it; hold Alt as you drop to skip keeping the transform relationship (the child holds its world position).
  Clear Parent — drag the child out of its parent's hierarchy to sever the link; holding Alt as you drop clears the parent yet keeps the parent's transform applied to the child.
  Parent Across Collections — to parent an object living in a different collection, hold Shift while dragging.
  See Parenting Objects for more on parenting and transform inheritance.
Note: drag-and-drop applies to the whole current selection; any selected data-blocks incompatible with the operation are left alone.

Modifiers, Constraints, and Visual Effects — the Outliner offers a few ways to handle these: drag individual items to reorder them within the stack or copy them to another object; drag the group item (Modifiers, say) to copy the entire stack onto another object, replacing that object's existing stack; and apply or delete items through the context menu.

Drag & Dropping to 3D Viewport — drag an object out of the Outliner into the 3D Viewport and you get a duplicate — a fresh object carrying its own copy of the source object data; drag object data instead and you get a linked duplicate — a fresh object pointing at that same source object data.

[Related references](INDEX.md).
