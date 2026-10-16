# Denoise Node

## Denoise Node

The Denoise node denoises renders from Cycles and other ray tracers, cutting render time by allowing fewer samples; it uses Open Image Denoise, which turns noisy images into clean ones with machine learning. Inputs: Image (the noisy input); Albedo (an optional albedo pass to better preserve detail — for Cycles, use the Denoising Albedo pass available with the Denoising Data passes); Normal (an optional normal pass, likewise the Denoising Normal pass); HDR (preserve colors outside the 0 to 1 range); Prefilter — None (no prefiltering, retaining the most detail and fastest but assuming noise-free inputs, which may need a high sample count, else noise remains), Fast (assumes noisy inputs but doesn't prefilter — faster than Accurate but blurrier), or Accurate (prefilter the inputs before denoising for more detail at more processing time); and Quality — Follow Scene (use the scene's setting), High (highest quality, long processing), Balanced (about half the time of High while keeping most quality), or Fast (quick output at a noticeable quality cost). Output: Image (the denoised result).

[Related references](INDEX.md).
