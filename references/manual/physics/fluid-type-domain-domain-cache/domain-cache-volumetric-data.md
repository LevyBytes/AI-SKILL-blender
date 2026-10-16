# Cache: Volumetric Data

### Volumetric Data

Format
Volume sim data storage (grids, particles).

Uni Cache :

Blender proprietary format with compression. Each object stores in its .uni file.

OpenVDB :

Sophisticated, effective format. All objects (grids, particles) in one .vdb per frame.

Compression OpenVDB Only
OpenVDB file compression.

Zip :

Zip-compressed files. Effective, slower than Blosc.

Blosc :

Blosc-compressed files. Multithreaded, similar size/quality to Zip.

None :

No compression.

Precision OpenVDB Only
OpenVDB data precision.

Full :

Full 32-bit precision.

Half :

Half 16-bit precision.

Mini :

Mini 8-bit where feasible; 16-bit otherwise.

Meshes Liquids Only
Mesh cache file format.

Binary Object: Compressed mesh files.
Object: Standard mesh data format.

Export Mantaflow Script
Exports the sim as standalone Mantaflow script when baking (bake "Bake Data"). Generally for developers/advanced users familiar with Mantaflow GUI. Debug Value 3001 enables.

[Related references](INDEX.md).
