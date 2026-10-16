# aud.Sound: accumulate(additive=False)

accumulate(additive=False)

Accumulates a sound by summing positive input differences to create a monotonic signal. With additivity enabled, negative differences also accumulate, and positive ones double.

Note that additivity breaks monotonicity.

Parameters:

additive – Whether accumulation is additive or not.

Returns:

The new Sound object.

Return type:

Sound
accumulate(additive=False)

Tallies sound by adding positive input changes to yield a monotonic output. With additivity on, negative changes contribute, and positive ones double.

Note that additivity removes monotonicity.

Parameters:

additive – Whether accumulation uses additivity.

Returns:

The new Sound object.

Return type:

Sound

[Related references](INDEX.md).
