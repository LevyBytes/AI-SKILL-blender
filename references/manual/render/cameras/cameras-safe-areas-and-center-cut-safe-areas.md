# Cameras: Safe Areas, Center-Cut Safe Areas

### Safe Areas 

Safe areas mark where to drop elements so a scene's vital content survives on screens of every kind.

Overscan differs from screen to screen, and old TV sets are the worst offenders.
So some content never reaches all viewers, because the band ringing the image edge stays hidden.
TV broadcasters answered this by defining two zones whose content is always shown: action safe and title safe.

Modern LCD and plasma sets run purely digital signals with zero Overscan, yet safe areas remain good practice and can be a broadcast legal requirement.

Inside Blender you open safe areas from either the Camera or the Sequencer view.

Red line: Action safe. Green line: Title safe. 

Tune the Safe Areas by their outer margin, a percentage of the run between center and render edge.
The camera view and the Video Sequence editor read the very same values.

Title Safe Margins X/Y
Also known as Graphics Safe .
Park all your key information, be it graphics or text, inside this zone so most viewers can take it in.

Action Safe Margins X/Y
Hold any notable action or character within this region.
Doubling as a screen "margin," it also keeps elements from bunching up against the edges.

Tip

Each nation lays down its own legal broadcast standard, and those specify, among plenty else, exact safe-area numbers.
Blender's safe-area defaults follow the EBU (European Union) standard.
Double-check you have the right figures before producing broadcast work, to sidestep trouble.

#### Center-Cut Safe Areas 

Center-cuts are an extra safe-area pair that keep content reading right on screens of a differing aspect ratio.
Feed an old TV 16:9 or 21:9 video and it lops off the sides.
Park content inside the center-cut zones so your composition's most important parts hold up on those screens.

Out of the box Blender draws a 4:3 (square) ratio sitting inside 16:9 (widescreen).

Cyan line: action center safe. Blue line: title center safe.

[Related references](INDEX.md).
