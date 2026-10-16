# Surface: Add Duplicate, Split, Separate

### Add Duplicate

Reference

Mode :

Edit Mode

Menu :

Surface ‣ Add Duplicate

Shortcut :

Shift - D

Copies the selected control points and builds a brand-new surface from them.
The fresh control points land in Move mode: drag the mouse to set
where they go, then click LMB to lock it in. Otherwise,
hit RMB or Esc to leave them where they started.

Keep in mind that your selection has to form one valid sub grid.
Otherwise the duplication aborts with an error.

### Split

Reference

Mode :

Edit Mode

Menu :

Surface ‣ Split

Shortcut :

Y

Detaches the selected sub grid from the rest of the surface while leaving it inside
the same Surface object. Border control points get copied, so the
original surface and the split-off one each keep their own.

For this to work, the sub grid has to be built from whole rows or whole columns of the surface grid — one or more of them.

### Separate

Reference

Mode :

Edit Mode

Menu :

Surface ‣ Separate

Shortcut :

P

Detaches the selected sub grid from the rest of the surface and relocates it into
a new Surface object. Border control points get copied, so the
original surface and the separated one each keep their own.

Again, the sub grid has to be made up of one or more entire rows or entire columns of the surface grid.

[Related references](INDEX.md).
