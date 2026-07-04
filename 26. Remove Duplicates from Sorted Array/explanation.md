
## Explanation 

**26. Remove Duplicates from Sorted Array**

In this problem we are given an array `nums`. The array is sorted in a non-decreasing order. We are tasked to remove the duplicate elements from `nums` **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)**. We are then to return the number of unique elements. 

Our approach is going to involve using two pointer, scanning the array from start to finish. 

We start by creating our pointers `k` and `i`. 

```Python
k = 0

for i in range(1, len(nums)):
```

We are going to be using `k` to keep track of the last unique value we encountered. We then use `i` to iterate through the array. If we encounter a value that differ from our as we iterate through `nums` we move `k` one step forward and copy our encountered value to that index. Doing this, we can know with certainty that each index equal or less than `k` will contain a unique value. 

```Python
    if nums[i] != nums[k]:
        k += 1 
        nums[k] = nums[i]
```

After we have processed the entire array, we need to return the number of unique elements. We know that each element with an index equal or smaller than `k` will be unique. In other words indexes  `[0]` to `[k]` are unique. Therefore the number of unique elements will be `k + 1`

```Python
return k + 1
```

**Time Complexity**

We pass through `nums` exactly `len(nums)` times. Inside our for loop we only do operations that has the average time complexity <code><i>O(1)</i></code>. Our solution will therefore have a time complexity of <code><i>O(n)</i></code>, where `n = len(nums)`.