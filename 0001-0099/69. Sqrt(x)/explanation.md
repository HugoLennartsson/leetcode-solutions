
## Explanation

**69. Sqrt(x)**

In this problem we are given a non-negative integer `x`. We are tasked to return the square root of `x` rounded down to the nearest integer. We are not allowed to use any built in exponent function or operator. 

Our approach for this problem is going to be using a slightly modified version of binary search to find the square root.

We can start by covering the special cases. If `x` is zero or one, `x` will be its on square root. So in these cases we can just return `x`.

```Python
if x < 2:
    return x
```

Now we start searching the range of integers between `2` and `x`. This is the smallest interval we are able to search where we are sure that the square root of `x` is located. 

```Python
    left, right = 2, x//2
    
    while left <= right: 
        mid = left + (right - left) // 2
```

Since we are searching for the square root of `x` we need to somehow determine when we have found it. To do this we square mid for each iteration. We use this value to compare to `x` and can by doing so figure our what side of mid the square root is located at. 

```Python
    num = mid * mid 

    if num == x:
        return mid
    elif num < x:
        left = mid + 1
    else:
        right = mid - 1 
```

If our loop exits without returning an integer, we know that our searched square root is not an integer value. In that case, we need to round it down to the nearest integer according to the problem description. Right before we exit the loop our left and right pointers are pointing at the same index. There are two possible cases going from here. The first one is that `num < x`, in that case we move left one step past right. Our left and right pointer are pointing at two consecutive integer values and we know that our square root is somewhere between these two. Since our left pointer has been moved to the greater integer and we were supposed to round down, we return right. In the second case `num > x`. In this case we move our right one step past our left. Here we find ourselves in the same situation as before, so we simply return right. 

```Python
return right
```

**Time Complexity**

This solution uses a version of binary search. Other than that we only use simple arithmetic operations and comparisons. This gives our solution the time complexity of <code><i>O(log(n))</i></code> where `n = len(x)`.

**Space Complexity**

In this solution we only make use of simple integer variables. The amount of variables stay the same no matter the input size. Our auxiliary space complexity is therefore <code><i>O(1)</i></code>.