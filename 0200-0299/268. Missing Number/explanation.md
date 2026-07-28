
## Explanation

**268. Missing Number**

In this problem, we are given an integer array `nums`. It contains distinct numbers in the range `[0, n]` with the exception of one number that is missing from the range. We are tasked to find and return that number.

The strategy we are going to be using is going to be using the length of the array to calculate the expected sum of the array. Then we subtract the actual sum from it to find the missing value.

We start by finding the length of our array.

```Python
length = len(nums)
```

Following, we calculate the expected sum of the input array. We do this by using Gauss's summation formula. $$\frac{n(n + 1)}{2}$$

```Python
expected_sum = (length * (length + 1)) // 2
```

After that, we can calculate the actual sum using the `sum()` function. 

```Python
actual_sum = sum(nums)
```

The missing number can be found by subtracting the actual sum from the expected sum. We return this.

```Python
return expected_sum - actual_sum
```

**Time Complexity**

The time complexity is determined by the size of the input array, since we need to sum each element in it. All other operations have constant time complexity. The solution has the time complexity <code><i>O(n)</i></code> where n is the length of the array.

**Space Complexity**

We only use integer variables to help us solve this problem. This gives us the space complexity of <code><i>O(1)</i></code>.


