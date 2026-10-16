# Adaptive Domain

## Adaptive Domain

### Adaptive Domain

Reference

Type :

Domain

Panel :

Physics ‣ Fluid ‣ Adaptive Domain

Enabling adaptive domain shrinks the boundary to envelope gas efficiently, reducing computation by omitting empty voxels. The original domain constrains expansion unless Add Resolution increases bounds.

Add Resolution
Voxels to append around domain exterior.

Margin
Empty space around gas in voxels. Fast-moving gas requires larger margins to prevent edge clipping but increases computation.

Threshold
Minimum gas density before a voxel registers as empty and exclusion occurs.

[Related references](INDEX.md).
