# Sampling: Path Guiding, Lights

### Path Guiding

Path guiding diminishes noise where light discovery proves difficult for regular path tracing—for instance, rooms lit through narrow portals. Important light orientations learn incrementally, refining with additional samples.

Note

- Path guiding requires CPU-only rendering.

- While path guiding aids caustic rendering in some cases, it is not optimized for intricate caustics as they resist guidance.

See also

Use Portals Area Lights for manual path trace direction.

Training Samples
Peak training sample count. Zero sustains training until render completion. Typically 128 to 256 training samples provide sufficient direction. More training slightly improves direction yet prolongs renders.

Surface
Activate surface diffuse and glossy path guiding.

Volume
Activate volume interior path guiding.

### Lights

Light Tree
Activate light tree for refined scene light sampling, evaluating position and intensity. May substantially lower noise at slightly extended per-sample duration.

Certain light properties are absent from the light tree: custom falloff, ray visibility, and intricate shader networks including textures. This can increase noise in scenes using these capabilities.

Light Threshold
Probabilistically skip light sampling when contribution falls below threshold. Avoids squandering samples on negligible-impact lights. Zero disables.

[Related references](INDEX.md).
