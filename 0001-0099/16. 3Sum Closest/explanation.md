
## Explanation

**16. 3Sum Closest**

In this problem we are given an array `nums` with the length `n` as well as an integer `target`. We are tasked to find the sum of values at three indices that is the closest to the integer `target`. We can also assume that each input has exactly one solution.

We start by sorting our input array. We also create a variable `n` to keep track of the length of the array. Then we initialize a variable `closest_sum` that we are going to use to keep track of the closest sum we have encountered so far as we iterate. 

```Python
nums.sort()
n = len(nums)
closest_sum = nums[0] + nums[1] + nums[2]
```

Now, for each number in the sorted array we check to the right of it for the closest three number sum to the target. We only need to check to the right of each number, since we can assume that the number our index is pointing to is always going to be the smallest element in the trio. 

```Python
for i in range(n - 2):
    left, right = i + 1, n - 1
```

We want to check for all of the numbers to the right of the index `i`, so we keep iterating until our `left` pointer and `right` pointer point at the same index.

```Python
    while left < right:
```

Now we calculate the sum of the values at the indexes `i`, `left` and `right`. If the sum is equal to our target, we can return `target`. If the sum is closer to target than our previously closest sum we update `closest_sum` to hold our `current_sum`. 

```Python
        current_sum = nums[i] + nums[left] + nums[right]

        if current_sum == target:
            return target
        
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum 
```

If our current sum is smaller than target, we need a larger value, so we move left one step to the right. if our current sum is larger than target we need a smaller value so we move right one step to the left.

```Python
        if current_sum < target: 
            left += 1
        else:
            right -= 1
```

Once we exit the loop, we have checked every valid combination, so we return the closest sum we have encountered.

```Python
return closest_sum
```

**Time Complexity**

For each number in the array, we have to iterate through each element to the right of it. This gives us a time complexity of <code><i>O(n&sup2;)</i></code>

**Space Complexity**

Timsort has a worst case space complexity of <code><i>O(n)</i></code>, this decides our space complexity.