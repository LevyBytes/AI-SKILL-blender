# Meta Strips

## Meta Strips

### Meta Strips

A Meta Strip bundles multiple strips into a single composite item.
This minimizes visual noise in the Sequencer and simplifies intricate workflows.
After formation, a Meta strip acts like any other and can shift, be resized, muted, or get effects.

Meta strips serve as organization aids.
When edits stack many overlapping or layered strips, grouping related ones into a Meta strip reduces clutter.

Make Meta Strip Ctrl - G
Choose all strips to bundle, then press Ctrl - G.
The new Meta spans from the earliest strip's start to the latest's end, collapsing channels into one.

UnMeta Strip Ctrl - Alt - G
Break apart a Meta strip to restore its contents to their original places and channels.
Useful for removing the Meta shell while preserving interior strips.

Example of Meta strips.

### Editing Meta Strips

Open a Meta strip with Tab to see only its contents.
The timeline switches to display the interior.

Press Tab once more to exit and return to the full timeline.

Meta strips may be nested within other Meta strips.
Pressing Tab goes out one level.
To exit more levels, ensure no Meta is active before pressing Tab.

Note

Meta strips default to Replace blending.
Depending on what's inside, visuals might differ from the source strips. Adjust the Meta's blend mode if needed.

### Use Cases

A frequent use is applying one effect to several clips.
For instance, if a shot spans multiple video files, bundle them in a Meta strip and add effects there instead of duplicating effects.

Meta strips also help structure sections—intros, sequences, graphics—as individual items.

See also

An Adjustment Layer effect strip achieves similar outcomes, applying effects to all strips below without bundling.

### Properties

Meta strips match other strip types in attributes.
Changes to Meta properties act on all contained strips as a group.

[Related references](INDEX.md).
