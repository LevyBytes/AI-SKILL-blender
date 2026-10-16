# imbuf.types.ImBuf

class imbuf.types. ImBuf
copy ( )

Hand back a copy of the image.

Returns :

A copy of the image.

Return type :

ImBuf
crop ( min , max )

Crop the image without making a copy.

Parameters :

- min ( tuple [ int , int ] ) – Minimum pixel coordinates (X, Y), inclusive.

- max ( tuple [ int , int ] ) – Maximum pixel coordinates (X, Y), inclusive.
free ( )

Release the image data right away (which makes any later use raise an error).
resize ( size , * , method = 'FAST' )

Resize the image without making a copy.

Parameters :

- size ( tuple [ int , int ] ) – New size.

- method ( str ) – Method of resizing (‘FAST’, ‘BILINEAR’).
channels

Number of color channels.

Type :

int
filepath

Filepath associated with this image.

Type :

str
planes

Number of bits per pixel.

Type :

int
ppm

Pixels per meter.

Type :

tuple[float, float]
size

Size of the image in pixels.

Type :

tuple[int, int]

[Related references](INDEX.md).
