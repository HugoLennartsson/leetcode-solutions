
## Explanation

**3637. Trionic Array I**

In this problem we are given an array `nums`. We are tasked to check if the array is trionic. 

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

- `nums[0...p]` is **strictly** increasing,
- `nums[p...q]` is **strictly** decreasing,
- `nums[q...n − 1]` is **strictly** increasing.

Our strategy is simple. We iterate through the array until it is not strictly increasing. When we find that it is not strictly increasing, we iterate until it is not is strictly decreasing. Then we keep iterating until it is not strictly increasing. If we have reached the end at this point, we know that the array is trionic.

We start by finding the length of our list. This will allow us to know when we have reached the end of the list.

```Python
n = len(nums)
```

We declare a variable `i`. We use this to compare an integer with the previous integer in the list. This is the method we use to check if the array is decreasing or increasing at certain points.

```Python
i = 1
```

Now we start checking for the first criteria, `nums[0...p]` is **strictly** increasing. We do this by iterating through the array until the values are not strictly increasing. If `i == 1` or `i == n` we know our array is not trionic. In the first case we know that the array does not start of strictly increasing. In the second case we know that the entire array is strictly increasing.

```Python
while i < n and nums[i] > nums[i - 1]:
    i += 1
if i == 1 or i == n:
    return False
```

We use the same logic for the second criteria, `nums[p...q]` is **strictly** decreasing. If we exit the loop and `i == n` we know that our array starts as strictly increasing and then transitions to and ends as strictly decreasing. 

```python
while i < n and nums[i] < nums[i - 1]:
    i += 1
if i == n:
    return False
```

Now we check for the third criteria, `nums[q...n − 1]` is **strictly** increasing. This is the same while loop we used for the first criteria. 

```Python
while i < n and nums[i]> nums[i - 1]:
    i += 1
```

Finally, after processing the entire array we need to somehow determine if it is trionic. When we have passed through all three of our while loops the array should be strictly increasing, then strictly decreasing and finally strictly increasing. If we exit our final while loop we can check if we have reached the end of the loop by comparing `i` to `n`. If they are equal we know that our array is trionic. If they are not equal, we know that the last part of the array is not strictly increasing.

```python
return i == n
```

**Time Complexity**

We iterate once though the input array. This gives us a linear time complexity, <code><i>O(n)</i></code>.

**Space Complexity**

We only use a few scalar variables regardless of the input size. We have constant space complexity, <code><i>O(1)</i></code>.