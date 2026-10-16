# Options

## Options

**Auto Normalize.**

Guarantees all deforming vertex groups total one during painting. When disabled, each point's weight can be any value between 0 and 1. However, when vertex groups serve as deform groups for character animation, Blender interprets weights comparatively, always normalizing across all deform bones. Operationally, strict normalization is unnecessary, and weight normalization does not disrupt animation playback.

This toggle proves most useful when re-normalizing while painting atop weights previously normalized via a different method.

[Related references](INDEX.md).
