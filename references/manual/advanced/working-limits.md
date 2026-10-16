# Working Limits

## Working Limits

Working limits. Space: object and vertex positions aren't clamped, but larger values grow steadily less precise. A table of scale versus accuracy: at 10, 1/1,048,576th; at 100, 1/131,072nd; at 1,000, 1/16,384th; at 10,000, 1/1,024th; at 100,000, 1/128th; and at 1,000,000, 1/16th. As a rough rule, values within -5,000 to +5,000 (a 10,000 range) are usually reliable, since single-precision floating-point math is used internally. Time: a scene currently allows at most 1,048,574 frames, giving continuous shots of 12 hours 8 minutes at 24 fps, 11 hours 39 minutes at 25 fps, 9 hours 42 minutes at 30 fps, and 4 hours 51 minutes at 60 fps; in practice a finished work usually combines many scenes, so this cap doesn't limit total length. Text fields: fixed-length strings are used internally (for data-block names, modifiers, vertex groups, UV layers, and so on); some common limits are directory 767, file-name 255, file-path 1023, and identifier 63, and because of multi-byte encoding some Unicode characters consume more than one ASCII character.

[Related references](INDEX.md).
