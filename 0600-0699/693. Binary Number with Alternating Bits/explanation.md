
## Explanation

**693. Binary Number with Alternating Bits**

In this problem we are given a positive integer. We are tasked to check if the integer has alternating bits.

We start by initializing a variable `x`. To construct `x` we use the `XOR` operation between our input integer and our input integer right shifted one step. If our input integer has alternating bits, `x` will have a binary representation that is only ones. This is because in an alternating binary number each bit will differ from its neighbor. If we right shift the input array, each bit will be the inverse of the original input given that they are alternating. 

```python
x = n ^ (n >> 1)
```

Based on what we said above, we now want to somehow check if the binary representation of `x` only contains ones. To do this we can use a cleaver trick. If you add `1` to a binary number that only contains ones will turn all of the `ones` into `0` and add a leading 1. If we then use an `AND` operation between `x + 1` and `x` the result will only be `0` if `x` is entirely made by `ones`. And since `x` will only be made of ones if `n` is alternating, an `AND` operation between `x + 1` and `x` will only return `0` if n is alternating. 

```python
return (x & (x + 1)) == 0
```

**Time Complexity**

We only use arithmetic operations in this solution, therefore our time complexity is <code><i>O(1)</i></code>.

**Space Complexity**

We use an integer variable, but no memory that scales with input size. The space complexity is <code><i>O(1)</i></code>.
