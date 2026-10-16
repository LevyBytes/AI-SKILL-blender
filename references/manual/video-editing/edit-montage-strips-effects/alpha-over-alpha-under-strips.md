# Alpha Over & Alpha Under Strips

## Alpha Over & Alpha Under Strips

### Alpha Over & Alpha Under Strips

Transparency info (the alpha layer) governs how this effect combines them.
Solid areas have alpha 1 (total opacity); transparent spots have alpha 0 (invisible).

Use Alpha Over / Alpha Under to layer CG components over footage.
Your 3D model sits as though filmed.
The Adjust ‣ Compositing ‣ Opacity sets how fully the top layer mixes, fading the overlay over the base.
Where the top is transparent, base colors show unchanged.

### Alpha Over

Alpha Over layers items in selection order; the first is ground, the second is foreground.
Opacity regulates foreground transparency. 0.0 shows only ground; 1.0 fully covers ground (except where foreground is see-through).

Warning

Press Premultiply Alpha in the Sidebar of the foreground strip to adjust how transparency combines.
Apply when overlaying a strip with mixed transparency (some see-through, some opaque, some partial) over a completely opaque strip. If edges glow or unexpected transparent spots appear, turn Premultiply on.

Alpha Over Effect.

### Alpha Under

Alpha Under reverses the layers: the first is foreground, the second is ground.
Opacity adjusts ground transparency. 0.0 shows only foreground; 1.0 matches Alpha Over.

[Related references](INDEX.md).
