# blf: blf. shadow ( fontid , level , r , g , b , a )

blf. shadow ( fontid , level , r , g , b , a ) 

Shadow options, enable/disable using SHADOW.

Parameters :

- fontid ( int ) – The id of the typeface as returned by blf.load(), for default font use 0.

- level ( int ) – The shadow type: 0 for none, 3 for 3x3 blur, 5 for 5x5 blur or 6 for outline. Other values raise a TypeError .

- r ( float ) – Shadow color (red channel 0.0 - 1.0).

- g ( float ) – Shadow color (green channel 0.0 - 1.0).

- b ( float ) – Shadow color (blue channel 0.0 - 1.0).

- a ( float ) – Shadow color (alpha channel 0.0 - 1.0).

[Related references](INDEX.md).
