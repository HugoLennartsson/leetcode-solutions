
## Explanation

**3634. Minimum Removals to Balance Array**

In this problem we are given an integer array `nums` and an integer `k`. We are tasked to find and return the minimum amount of elements to remove in order to make `nums` balanced. The array is considered balanced if the value of its maximum element is at most `k` times the minimum of the element.

Our strategy for this problem is going to start with sorting the array. Then we will use two pointers to create a sliding window over the array. We want to find the longest contiguous subarray. This is based on the idea, that if we decide to keep some maximum and minimum we can just keep the elements in between. This, because the biggest numerical difference between elements will be between the maximum and minimum. The values between automatically qualify as valid if the maximum and minimum do. 

We start by sorting the input array

```python
nums.sort()
```

Then we want to create two pointers, `left` and `right`. We also declare a variable `max_window` in order to keep track of the length of the maximum contiguous subarray we have found so far. 

```python
n = len(nums)
max_window = 0
left = 0

for right in range(n):
```

Inside the for loop, `right` represents the index of the current maximum of the window. The variable `left` represents the index of the current minimum of the window. The condition we are looking for is `nums[left] * k < nums[right]`. If this condition is violated, the minimum is too small relative to the maximum. In that case we shrink the window by moving `left` one step forward. 

```python
    while nums[left] * k < nums[right]:
        left += 1
```

We use `max_window` to track the largest window encountered. Since we check if the window is valid on the lines above, we know that the window created by `left` and `right` will be a balanced subarray. If the new window is larger we save it as the current max window. 

```python
        max_window = max(max_window, right - left + 1)
```

Then when we have iterated through each balanced subarray we return the difference of the input arrays length and the length of the subarray. In other words the amount of elements we need to remove.ks

```python
    return n - max_window 
```

**Time Complexity**

The `.sort()` function has a time complexity of `O(nlog(n))`. The sliding window will have the time complexity `O(n)`, since the total work across all iterations of the while loop is bounded by n. The final complexity will therefore be `O(nlog(n))` + `O(n)` = `O(nlog(n))`