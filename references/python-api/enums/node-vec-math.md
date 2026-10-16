# Node Vec Math Items

| Value | Meaning |
| --- | --- |
| `ADD` | Add.<br>A + B. |
| `SUBTRACT` | Subtract.<br>A - B. |
| `MULTIPLY` | Multiply.<br>Entry-wise multiply. |
| `DIVIDE` | Divide.<br>Entry-wise divide. |
| `MULTIPLY_ADD` | Multiply Add.<br>A * B + C. |
| `CROSS_PRODUCT` | Cross Product.<br>A cross B. |
| `PROJECT` | Project.<br>Project A onto B. |
| `REFLECT` | Reflect.<br>Bounce A across the normal B; B need not be normalized.. |
| `REFRACT` | Refract.<br>Given an incident vector A, a surface normal B and an index-of-refraction ratio Ior, hand back the refracted vector R. |
| `FACEFORWARD` | Faceforward.<br>Flip vector A so it faces away from surface B per its normal C; yields (dot(B, C) < 0) ? A : -A. |
| `DOT_PRODUCT` | Dot Product.<br>A dot B. |
| `DISTANCE` | Distance.<br>Distance between A and B. |
| `LENGTH` | Length.<br>Length of A. |
| `SCALE` | Scale.<br>A multiplied by Scale. |
| `NORMALIZE` | Normalize.<br>Normalize A. |
| `ABSOLUTE` | Absolute.<br>Entry-wise absolute. |
| `POWER` | Power.<br>Entry-wise power. |
| `SIGN` | Sign.<br>Entry-wise sign. |
| `MINIMUM` | Minimum.<br>Entry-wise minimum. |
| `MAXIMUM` | Maximum.<br>Entry-wise maximum. |
| `ROUND` | Round.<br>Per entry, snap to the closest integer, sending a .5 fraction upward. |
| `FLOOR` | Floor.<br>Entry-wise floor. |
| `CEIL` | Ceil.<br>Entry-wise ceil. |
| `FRACTION` | Fraction.<br>The fraction part of A entry-wise. |
| `MODULO` | Modulo.<br>Entry-wise modulo using fmod(A,B). |
| `WRAP` | Wrap.<br>Entry-wise wrap(A,B). |
| `SNAP` | Snap.<br>Bring A down to the greatest multiple of B that does not exceed it. |
| `SINE` | Sine.<br>Entry-wise sin(A). |
| `COSINE` | Cosine.<br>Entry-wise cos(A). |
| `TANGENT` | Tangent.<br>Entry-wise tan(A). |

[Related references](INDEX.md).
