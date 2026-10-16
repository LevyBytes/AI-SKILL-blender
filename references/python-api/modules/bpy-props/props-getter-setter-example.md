# bpy.props: Getter/Setter Example

### Getter/Setter Example 

Accessor operations may be utilized for boolean, integer, floating point, sequence and pick qualities.

If get or set functions are laid out, the quality will not be held in the ID qualities
instantly. Rather, the get and set operations will be termed when the quality
is correspondingly examined or penned from the interface, and are answerable to handle the information retention.

Keep in mind that:

- It is improper to lay out a set operation without a coordinating get single.

- When a get operation is laid out but no set sole, the quality is read-only.

get_transform and set_transform may be utilized when the yielded worth must be improved,
yet the ordinary interior retention is yet applied. They may exclusively modify the worth before it is
prepared or supplied, yet do not manage how/where that material is held.

Note

It is feasible to lay out both get / set and get_transform / set_transform operations
for the matching quality. In application, yet, this must infrequently be wanted, as almost all 'modify'
procedure may additionally occur within a get / set operation.

Warning

Keep in mind that these functions may be carried out in concurrent framework.

Warning

Take caution when obtaining further qualities in these operations, as it may quickly set off
difficult matters, for instance unending patterns (if e.g. two qualities strive to additionally prepare the alternate
quality's worth in their own set operation), or unexpected side-effects due to shifts
in information, prompted e.g. by an upgrade operation.

[Related references](INDEX.md).
