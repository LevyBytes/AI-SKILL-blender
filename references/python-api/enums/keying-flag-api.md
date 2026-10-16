# Keying Flag Api Items

## Keying Flag Api Items

### Keying Flag Api Items

`INSERTKEY_NEEDED` :

Only Needed.

Add keyframes solely on the F-Curves that actually require them.

`INSERTKEY_VISUAL` :

Visual Keying.

Key from the evaluated 'visual transforms' rather than the raw values.

`INSERTKEY_REPLACE` :

Replace Existing.

Update keyframes that are already present and add none.

`INSERTKEY_AVAILABLE` :

Only Available.

Skip making new F-Curves for channels that have none yet.

`INSERTKEY_CYCLE_AWARE` :

Cycle Aware Keying.

For a curve set to cyclic extrapolation, fold the keyframe back into the cycle's time span, and when an end key changes, sync its counterpart too.

[Related references](INDEX.md).
