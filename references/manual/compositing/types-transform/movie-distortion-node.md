# Movie Distortion Node

## Movie Distortion Node

Real camera lenses all produce some lens distortion, but a render has none, so the Movie Distortion node either removes distortion from movies or adds it to a render so the render blends with the clip — usually during motion tracking. Calculating distortion: first compute the clip's lens distortion by adjusting K1, K2, and K3 in Movie Clip Editor ‣ Properties ‣ Lens. Inputs: Image (standard color input) and Type — Undistort (undistort the image, usually for the raw distorted clip) or Distort (distort the image, usually for rendered images). Properties: Movie Clip (the clip whose distortion to use, useful when several clips have different distortion settings; see the Data-Block Menu). Output: Image (after distorting/undistorting). Distortion vs undistortion: both produce similar results but differ — for a clip bulging out, distort the render and leave the clip alone, since undistorting it would need extra pixel information Blender lacks; for a clip bulging in, undistort the clip and leave the render, since distorting it would need those unavailable pixels — and doing the wrong one gives weird edges.

[Related references](INDEX.md).
