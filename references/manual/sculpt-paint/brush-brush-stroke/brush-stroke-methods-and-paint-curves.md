# Brush stroke methods and paint curves

Stroke settings determine where and how a brush applies paint or sculpting dabs. Other brush effects build on this behavior.

## Stroke Method

Choose the method with `Alt-E`.

- Dots applies paint at each mouse movement step. Distance between steps is not used, so slower movement can accumulate more strength.
- Drag Dot places one dab and lets you position it by dragging.
- Space places successive dabs at the distance controlled by Spacing.
- Airbrush continues applying paint while the mouse button is held; Rate controls the interval between applications.
- Anchored places one dab; dragging changes its diameter. Edge to Edge uses the initial click and dragged position as opposite points on the circle.
- Line draws a screen-space line. Dabs follow Spacing; hold `Alt` to constrain the line to 45-degree increments.
- Curve follows a Bézier Paint Curve, placing dabs according to Spacing.

Spacing is measured as a percentage of the brush radius. Enable its pressure sensitivity control to vary spacing with tablet pressure.

## Paint Curves

Paint Curves are reusable data-blocks selected through the data-block menu.

- Use `Ctrl-RMB` to create the first point and add further points. Drag to set handles. The stroke follows point creation order.
- Drag points and handles with `RMB`, or `LMB` with right-click selection. Use `Shift-RMB` for symmetrical handles.
- Transform selected points with `G` to move, `R` to rotate, and `S` to scale.
- Select individual handles with `LMB`, or `RMB` with right-click selection. Extend selection with `Shift-LMB`; `A` selects or deselects all.
- Delete a point with `X`.
- Execute the stroke with `Return` or Draw Curve. `Ctrl-LMB` is an alternative; with right-click selection, use `LMB`.

[Related references](INDEX.md).
