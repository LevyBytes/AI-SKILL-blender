# Evaluate at Index Node

## Evaluate at Index Node

### Evaluate at Index Node

Access geometry element data by index; similar to Sample Index.
Differs: uses field context geometry (no geometry input).

Also similar to Evaluate on Domain: but specifies retrieval by index instead of auto domain interpolation.

### Inputs

**Index**
Element position in the domain to fetch (e.g. "the fourth face", "the first control point").

**Value**
Field source.

### Properties

**Domain**
Evaluation domain.
Useful for domain mismatch (e.g. pick vertex per face).

### Output

**Value**
Field value at the index.

[Related references](INDEX.md).
