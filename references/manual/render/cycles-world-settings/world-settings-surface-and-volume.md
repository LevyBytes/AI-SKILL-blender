# World Settings: Surface, Volume, Light Group

### Surface

Sampling
World material sampling technique. Auto or Manual enable Multiple Importance Sampling while None disables. Multiple Importance Sampling favors lighter texture regions, reducing render noise at artifact risk (Fireflies). Enable with textured small-area lights (like suns) for faster convergence.

Below: Multiple Importance Sample off versus on. Both render 25 seconds (Off: 1,500 samples, On: 1,000).

| Description | Description |
| --- | --- |
| Multiple Importance Sample off. | Multiple Importance Sample on. |

Map Resolution
Importance map resolution. Higher resolution captures fine features and samples accurately, consuming more memory, rendering slightly slower. May lower noise with high-res images.

Max Bounces
Backdrop light bounce limit in rendering.

See also

See Reducing Noise for additional reduction guidance.

Shadow Caustics
Flag World Shader as refractive caustic source. Pairs with Cast and Receive caustic object settings for selective refractive caustic acceleration.

### Volume

Sampling Method

Distance :

Dense volumes lit from afar: Distance proves most effective. Typically unused for World volumes.

Equiangular :

Light inside/near volume: equiangular suits better.

Multiple Importance :

Mixed conditions: multiple importance optimal.

Interpolation
Volume interpolation approach.

Linear :

Basic interpolation, suited to thin volumes.

Cubic :

Refined high-detail interpolation for dense volumes, slower.

Step Size Biased
World volume shader sample spacing. Only active with Render ‣ Volumes ‣ Biased enabled. See Volume Render Settings.

### Light Group

Light Group Cycles only
Add the current World Surface Shader to the chosen Light Group.

Add Light Group
Pressing this generates a Light Group matching the name input field and assigns this World Shader to it if the name lacks an existing group.

[Related references](INDEX.md).
