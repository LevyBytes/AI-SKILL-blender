# Sampling: Advanced

### Advanced

Pattern
Integrator random sample sequence.

Automatic :

Blue-Noise (below), adjusted for viewport to improve early-sample quality. Aids interactive adjustments (view shifts, object moves...) during constant restarts.

Classic :

Owen-scrambled Sobol precomputed sequences.

Blue-Noise :
Blue-noise sequence optimizing frequency balance. Full samples typically appear smoother than Classic despite equal noise magnitude.

Seed
Integrator seed for alternative noise layouts.

Use Animated Seed
Seed adjustment per-frame. Enable for animation to reduce pattern visibility through variation.

Scrambling Distance
Reduces inter-pixel randomness to boost GPU rendering, accepting potential artifacts. Incompatible with Blue-Noise sampling.

Automatic
Adapts scrambling via sample count.

Viewport
Uses scrambling distance for viewport rendering, accelerating but risking flicker.

Multiplier
Scrambling distance multiplier. Below one reduces distance, potentially accelerating GPU work yet increasing artifact visibility.

Min Light Bounces
Minimal light bounces per-path, thereafter Russian Roulette probabilistically halts paths contributing minimally. Higher settings yield less noise, potentially lengthening render duration. For low maximum bounces, match minimum bounces.

Min Transparent Bounces
Minimum transparent bounces (passthroughs). Higher values reduce opening-bounce noise but may reduce effectiveness for complex shapes like hair and volumes.

Layer Samples
Controls View Layer Sample Override application.

Use :

Permit layer overrides of scene sample count.

Bounded :

Allow overrides not exceeding scene sample count.

Ignore :

Overlook overrides.

Sample Subset
Render a partial sample count. Multiple subset renders combine into totals via Python Console:

bpy.ops.cycles.merge_images(input_filepath1=r"1.exr", input_filepath2=r"2.exr",
output_filepath=r"combined.exr")

Typical use: spread frame rendering over machines. Example: 2048 total samples across two systems:

- Both: set (Max) Samples to 2048, disable Denoise , activate Sample Subset .

- Machine 1: Offset 0, Length 1024.

- Machine 2: Offset 1024, Length 1024.

- Run 1024-sample renders on each, merge results for 2048-sample equivalent.

Offset
Zero-indexed first sample position in subset.

Length
Subset sample count. This overrides (Max) Samples for rendering samples, but (Max) Samples must still match total subset samples—mismatched noise creates inferior merges.

[Related references](INDEX.md).
