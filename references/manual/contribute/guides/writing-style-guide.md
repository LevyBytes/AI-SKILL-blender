# Writing Style Guide

## Writing Style Guide

Primary goals — the manual aims to be: User Focused (written for people educated in computer graphics who grasp 3D basics and/or know other 3D software, yet kept understandable to non-technical users even where the topic is highly technical); Complete (a detailed functional description of every feature, tool, and option — though not every tiny detail, since each key area has a canonical source of truth; cover what a feature is, how to use it, and its purpose, adding background only when needed for deeper understanding of a 3D pipeline); Concise (computer graphics is full of rules, exceptions, and interesting details, but expanding into them adds unnecessary content, so keep the text concise and relevant to the end user); and Maintainable (Blender releases often, so write content that won't need redoing the moment a small change lands, which also helps a small documentation community keep up). Content guidelines — keep this page in mind and deviate only with good reason; when in doubt, check with the documentation team on Blender Chat. Rules of thumb: spell-checking is strongly recommended; use American English (modeling not modelling, color not colour, and number formatting like 2,718.28 not 2 718,28); mind grammar, wording, and simple English; keep sentences short and clear; explaining why or how an option is useful is a good idea; if unsure how a feature works, ask someone or find and ask its developer; and wrap RST files at column 120, with no line exceeding it. To be avoided: first-person writing, your own opinions, weasel words, and needless vagueness (e.g. "Reloading the file will probably fix the problem," "Most people do not use this option because…"); specific, quickly-outdated details (e.g. "Blender has 23 different kinds of modifiers," "Enabling previews adds 65536 bytes to each blend-file unless compressed"); documenting bugs (Blender fixes hundreds between releases, so the manual can't keep up — known unresolved issues can be documented as Known Limitations or in troubleshooting); product placements or promoting software/hardware brands (keep content vendor-neutral); mathematical/algorithmic implementation details when a simpler explanation exists (e.g. mesh-smoothing internals are unnecessary, but a Mix node's blend types do need a mathematical explanation); repeating large blocks of text (explain once, then refer back, and for general terminology define a :term: in the glossary); listing every menu option such as frame rates (summarize or omit, since such lists only restate the interface and are a lot to read and maintain); documenting release-to-release changes (that's what release notes are for — document only Blender's current state); naming a value's unit unless it's obscure and unpredictable; and copying Blender's tooltips verbatim (people come to the manual to learn more than the UI offers — as a last resort, add a comment, hidden from the HTML but useful to editors):
```text
.. TODO how does this tool work? ask Joe Blogg.
```
Glossary — for the Glossary section defining common Blender and computer-graphics terms: define the term before any further information; avoid constructs like "it is" or "xyz is" before the definition; don't repeat the term immediately or use it in its own definition; don't add terms absent from Blender's interface or the manual; avoid overly long entries (supplement complex terms with external links); avoid duplicating documentation (if explaining the term is another section's main focus — e.g. a tool name — just link there, or skip the glossary entry); and put URL references at the end, e.g.:
```text
See also `OpenGL `__ on Wikipedia.
```
Examples - this entry:
```text
Displacement Mapping
   Uses a grayscale heightmap, like Bump Mapping,
   but the image is used to physically move the vertices of the mesh at render time.
   This is of course only useful if the mesh has large amounts of vertices.
```
would instead be written definition-first:
```text
Displacement Mapping
   Distorts vertices with an image.
   Similar to Bump Mapping, but operates on the mesh's geometry.
   The mesh must have enough geometry.
```
And this entry:
```text
Doppler Effect
   The Doppler effect is the change in pitch that occurs
   when a sound has a velocity relative to the listener.
```
would be written to avoid the immediate repetition of the term:

```text
Doppler Effect
   Perceived change in pitch that occurs
   when the source of a sound is moving relative to the listener.
```
This entry:
```text
Curve
   It is a class of objects.
   In Blender there are Bézier curves and NURBS curves.
```
would be written to avoid the "it is":
```text
Curve
   A line interpolated between Control Vertices.
   Common types include Bézier and NURBS.
```

[Related references](INDEX.md).
