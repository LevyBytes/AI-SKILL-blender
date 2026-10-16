# Visibility, Masking & Face Sets

## Visibility, Masking & Face Sets

### Visibility, Masking & Face Sets

### Visibility Control

Mesh sections can be concealed in Sculpt Mode. Since hidden faces cannot be sculpted, this feature helps you concentrate on specific regions. Concealing geometry also enhances rendering performance in the viewport.

Hiding applies consistently across all modes except Object Mode (concealing faces in one mode hides the same faces in other modes too).

In contrast to Selection Masking in other painting tools, Sculpt Mode relies primarily on Masks and Face Sets to manage mesh display and control which regions can be modified. The Clipping Region is an exception and functions across any mode.

Common navigation shortcuts include pressing H to conceal the active face set beneath the cursor, plus Shift - H for solo-viewing (or exposing all regions).

Toggling visibility state and displaying all content is available from the Alt - W pie menu.

Adjusting visibility can also be accomplished with the Hide Gesture Tools.

See also

Consult Show & Hide for additional visibility control options.

### Masks

A mask restricts which mesh vertices are affected by sculpting and painting operations. Masks are created or adjusted via the Mask Gesture Tools and Mask by Color tool.

The internal representation of masks relies on the sculpt_mask Attributes storage system.

### Clear & Invert

Mask creation uses a different conceptual approach compared to selection in other modes. For instance, Shift - LMB performs smoothing rather than extending a mask.

Masking is also reversed from selection (masked vertices cannot be edited, while selected vertices can be).

A mask is typically added to the existing mask with LMB and removed with Ctrl - LMB. To edit the masked regions, apply the Invert operator. When masking all visible geometry, the recommended approach is to Clear the mask first, then Invert.

Both operations are accessible from the A pie menu.

See also

Explore the Mask Menu for additional mask management options.

### Face Sets

Face sets organize your mesh into distinctly colored groups of faces for quick visibility toggling as previously mentioned. They also facilitate rapid mask creation via the Mask Expand feature. The Face Set Expand function is useful for creating, adjusting, and combining face sets.

Further options are available in the Alt - W pie menu.

Face Sets can be created and modified using the Draw Face Sets brush, Mask Gesture Tools. The Edit Face Set tool provides additional modification capabilities.

See also

Visit the Face Sets Menu for comprehensive face set management information.

Face sets use the sculpt_face_set Attributes for internal storage.

### Auto-Masking

Auto-Masking is an efficient method to target specific mesh regions without manually establishing a mask or concealing geometry. This feature proves particularly effective when combined with face sets.

### Display Settings

The visibility and appearance of masks and face sets are customizable in the Display Settings panel.

[Related references](INDEX.md).
