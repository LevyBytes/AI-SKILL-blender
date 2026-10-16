# Volume Displace Modifier

## Volume Displace Modifier

Volume Displace is available exclusively for Volume Objects.

The Volume Displace modifier shifts existing volume grids based on a 3D texture, using the RGB channels to displace into X, Y, and Z directions respectively.

Texture specifies the evaluated texture at every voxel.

Note: grayscale textures stretch along one axis. Color textures work better.

Strength controls displacement magnitude.

Sample Radius affects quality and performance—smaller values run faster but may clip the volume exterior. Keeping displaced volumes near their original position is important for performance.

Mid Level compensates when the texture causes a directional bias toward one side, allowing the displaced region to return to center.

[Related references](INDEX.md).
