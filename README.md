# multi-simd-cmp-permutations

This is some code to help work out if my thoughts on [simd accelerated control flow](https://github.com/samsquire/simd-accelerated-control-flow) is possible.

The idea is that we can run multiple SIMD CMP sequentially and subtract them all and then map that to a permutation of straight line control flow.

There should be no duplicates from subtracting CMPs.