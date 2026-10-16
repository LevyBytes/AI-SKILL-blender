# Movie Clip Node

## Movie Clip Node

The Movie Clip node draws values from footage cameras and tracking and links them to its outputs — image sequences can be loaded, but only the Image and Alpha values are available then, since the other outputs have no associated values, while a tracked clip lets Blender fill the outputs from internal tracking values (with the start/end frames defined in the Movie Clip editor). It has no input sockets. Properties: Movie Clip (select the clip; for controls see the Data-Block Menu). Outputs (the first two are the minimum): Image (the whole image in the specified color space), Alpha (the alpha from the movie or image), Offset X and Offset Y (the X/Y offset from the footage camera or tracking), Scale (the image scale from them), and Angle (the lens angle from them).

[Related references](INDEX.md).
