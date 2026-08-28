# Parallelism Policy

Parallelize independent read-heavy work and genuinely disjoint implementation slices.

At most one active writer owns a write-critical file/module. Every parallel implementation task needs explicit non-overlapping ownership. If scopes overlap, sequence writers or let one write while the other returns recommendations.

The main thread owns shared coordination state and final integration. Do not parallelize tightly coupled tasks simply to increase agent count.
