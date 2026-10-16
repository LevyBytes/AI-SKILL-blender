# File Path Foreach Flag Items

## File Path Foreach Flag Items

### File Path Foreach Flag Items

`SKIP_LINKED` :

Skip Linked.

Pass over the paths belonging to linked IDs.

`SKIP_PACKED` :

Skip Packed.

Pass over paths whose matching data has been packed.

`RESOLVE_TOKEN` :

Resolve Token.

Expand the tokens in a virtual filepath down to one concrete filepath. For now this only applies to UDIM tiles.

`SKIP_WEAK_REFERENCES` :

Skip Weak References.

Pass over weak reference paths. Such paths are usually handy extras rather than something the current .blend file actually reads data from.

`SKIP_MULTIFILE` :

Skip Multi-file.

Pass over paths where one directory backs an array of files, such as image sequence strips or point caches. Only the first path gets handled in that case, which matters for directory-manipulation callbacks that would otherwise touch the same directory over and over.

`RELOAD_EDITED` :

Reload Edited.

Reload the data whenever its path is changed.

[Related references](INDEX.md).
