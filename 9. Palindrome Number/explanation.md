
## Explanation 

**9. Palindrome Number**

In this problem we are tasked to construct a function that checks if an integer `x` is palindrome. A palindrome number is a number that reads the same `forwards` and `backwards`. It is also requested that we solve the problem without converting `x` to a string. 

We start by dealing with the edge cases. A number cannot be palindrome if it is negative or if it ends with `0`. 

```Python
if x < 0 or (x % 10 == 0 and x!=0):
    return False
```

The main strategy that we are going to be using to check if the integer is palindrome is storing half of the integer reversed in a variable. As we write to that variable we keep on removing the last digit of `x`. We keep on doing this until we reach the middle digit/digits of `x`.

We create a variable `reversed_half` to store the reverse half. 

```Python
reversed_half = 0
```

We then begin processing `x` from the back to the front. We limit our while loop to stop when `x` is no longer larger than `reversed_half`. 

```Python
while x > reversed_half:
```

Each iteration of the loop we add the last digit in `x` as the last digit in `reversed_half`. We then remove the last digit of `x` by performing integer division by `10`. This moves each digit one step backwards. 

```Python
    reversed_half = reversed_half * 10 + x % 10
    x //= 10
```

Once we exit the loop there are two possible scenarios. If `x` was even we will have two integers of equal length. In this case we can simply compare the two. If it was odd, `reversed_half` will be one digit larger. However, the extra digit at the end of `reversed_half` will be the middle point of the original integer. This means that it is not needed in order to determine if the integer is palindrome. In this case we just perform integer division by `10` on `reversed_half` and then compare it with `x`.

```Python
return x == reversed_half or x == reversed_half // 10
```

**Time Complexity**

In this problem we iterate through half of the integer. The amount of digits in `x` can be expressed as `log₁₀ x`. The time complexity of the solution will therefore be <code><i>O(log₁₀ x)</i></code>.

**Space Complexity** 

Using this approach we only rely on a single extra variable `reverse_half` to store the second half of the number. We do not rely on any auxiliary data structures that scale with the input size. This means that the amount of memory used remains constant regardless of our input size. Therefore our space complexity will be <code><i>O(1)</i></code>.