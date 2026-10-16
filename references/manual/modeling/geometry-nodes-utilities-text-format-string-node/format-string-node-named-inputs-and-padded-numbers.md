# Format String Node: Named Inputs, Padded Numbers, Number Format (Template Style), Path with Frame Number

### Named Inputs

Format: `Size: {width} x {height}`
Inputs: width=1920, height=1080
Result: `Size: 1920 x 1080`

### Padded Numbers

Format: `Frame_{:04}`
Inputs: Integer 12
Result: `Frame_0012`

### Number Format (Template Style)

Format: `##.00`
Input: Float 3.1415
Result: `03.14`

### Path with Frame Number

Format: `/output/image_{:04}.png`
Input: Integer 42
Result: `/output/image_0042.png`

[Related references](INDEX.md).
