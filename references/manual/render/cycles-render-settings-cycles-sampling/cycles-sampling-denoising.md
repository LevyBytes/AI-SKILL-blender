# Sampling: Denoising

### Denoising

Denoising employs a dedicated algorithm achieving cleaner results without higher sample counts.

See also

Activating the Denoising Data render pass enables post-render denoising through the Denoise Node in compositing.

Denoise (Viewport)
Activate denoising in Rendered viewport shading mode.

Denoise (Render)
Activate denoising for final rendering.

Denoiser
Algorithm selection.

Automatic :

Uses GPU acceleration when available for best performance. Favors OpenImageDenoise over OptiX.

OpenImageDenoise :

Intel's Open Image Denoise, an AI-based denoiser. Typically delivers top-tier quality.

OptiX :

NVIDIA's OptiX AI denoiser. Some older NVIDIA GPUs without OpenImageDenoise support benefit. Only accessible with OptiX configuration in Cycles Render Devices preferences.

Passes
Render pass inputs for the denoiser. More inputs typically improve outcomes. Albedo minimum is advised to prevent detail blur at lower samples.

None :

Color-only denoising.

Albedo :

Color and albedo denoising.

Albedo + Normal :

Color, albedo, and normal denoising.

Prefilter OpenImageDenoise
Prefilter application to inputs prior to denoising. Visible only with OpenImageDenoise .

None :

No input prefiltering. Maximum detail retention, fastest execution, assumes noise-free inputs, demanding high sample counts. Noise persists without noise-free inputs.

Fast :

Non-prefiltered inputs, accepting noise, faster than Accurate, yielding blurrier results.

Accurate :

Input prefiltering reduces noise prior to denoising, typically sharper than Fast, extending processing time.

Quality OpenImageDenoise
Overall denoising excellence. Visible only with OpenImageDenoise .

High :

Top-tier output, extended processing.

Balanced :

Speed and quality middle ground.

Fast :

Speed-prioritized (viewport rendering ideal).

Start Sample
Initial sample for viewport denoising.

Use GPU
Perform denoising on the GPU. Substantially outpaces CPU, demanding GPU memory. Disable when GPU memory is exhausted by large scenes.

Consult GPU Rendering for supported GPU information.

[Related references](INDEX.md).
