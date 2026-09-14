
## Explanation

**231. Power of Two**

In this problem we are given an integer `n`. We are tasked to return `True` if the integer is a power of two. Otherwise `False`. It is also hinted at that there is a possible solution not using loops or recursion.

We can use a little trick to solve this problem. Each integer has a binary representation. In binary, each digit represents 2 to the power of the digits position. Using that, we know that each binary representation of a power of two will have exactly one digit set to `1` and all of the others set to `0`. We use this in our solution.

First we check if `n` is a positive number, since all numbers that are a power of 2 are positive. Then we to figure out how to check if the binary representation of the integer has one digit set to `1` and all the others set to `0`. We can do this by conducting a bitwise `AND` between the `n` and `n - 1`. If n is a power of two, we know that its most significant bit is `1` and all the others are `0`. If we subtract 1 from this number, its most significant bit will be set to `0` and all of the other ones will be set to `1`. This is because each of the digits will have to borrow from the digit one step more significant than itself. It will create a chain until it reaches the most significant digit. That digit will be borrowed. Our bitwise `AND` will result in `0` if this is the case, since `n - 1` will be the inverse of `n`. We use this as our second condition. 

```Python
return n > 0 and (n & (n - 1)) == 0 
```

**Time Complexity**

We only make use of operations that require constant time, the time complexity is <code><i>O(1)</i></code>.

**Space Complexity**

We perform the operations directly on the input parameter, this gives us constant space complexity <code><i>O(1)</i></code>. 