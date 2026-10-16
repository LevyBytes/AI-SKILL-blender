# Sampling: Adaptive Sampling

## Sampling

### Sampling

Reference

Panel :

Render ‣ Sampling

Sampling traces rays from the camera into the environment, bouncing until striking a light source—a Light object, emissive mesh, or world backdrop. This ray-tracing method is termed the integrator.

Viewport (Max) Samples
Per-pixel sample count in the 3D Viewport (Rendered shading mode). Zero activates indefinite sampling.

Render (Max) Samples
Per-pixel path count in final rendering. Higher counts yield cleaner results, requiring longer computation.

Time Limit
Halts rendering upon exceeding the time threshold, even if sample targets remain unmet. Zero disables the limit.

Note

Time limit excludes preprocessing—only active render time counts.

### Adaptive Sampling

When Noise Threshold activates, Cycles applies adaptive sampling, curtailing sampling in areas sufficiently clean versus the threshold—avoiding effort on satisfactory regions. Example: character hair may require many samples, yet the background needs few.

Noise Threshold
Quality cutoff for continuing sample investment per pixel. Standard ranges: 0.1 to 0.001, with lower thresholds ensuring superior quality but extended renders. Zero makes Cycles set an automatic threshold from total sample count.

Min Samples
Minimum samples per pixel before adaptive sampling engages. At 0 (default), Cycles picks based on the Noise Threshold .

[Related references](INDEX.md).
