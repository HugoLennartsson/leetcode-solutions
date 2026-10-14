
## Explanation

**15. 3Sum**

In this problem we are given an integer array nums, we are tasked to find and return all of the triplets that sum up to 0. 

Our approach is going to involve sorting the array, and then by doing so we can make a few assumptions that will make the process a bit easier. 

```Python
res = []
nums.sort()
```

We start looping through the sorted list, processing each element expect the last two. This will ensure that we always have two elements to the right of `i`. The reason for this will become apparent later on. 

```Python
for i in range(len(nums) - 2):
```

For the numbers we are checking, we want our number at index `i` to be negative or zero. This is because we are going to be checking the numbers to the right of the number at index `i`. Three positive numbers cannot sum to $0$.

```Python
    if nums[i] > 0:
        break
```

To avoid duplicate triplets, we can make sure that we only search for possible solutions once for each negative number. We can do this by checking of our current number is equal to the next number in the sorted array. 

```Python
    if i > 0 and nums[i] == nums[i - 1]:
        continue
```

Now we create two pointers, one that points at the index one step after `i` and one that points at the last index in the array. We want to look for a combination where the numbers at index `i`, `left` and `right` adds up to zero. We call this sum `s`.

```Python
    left, right = i + 1, len(nums) - 1
    while left < right:
        s = nums[i] + nums[left] + nums[right]
```

If we find the combination mentioned above, we add it to `res` and move our left and right pointers until they point at different values than they did before. 

```Python
        if s == 0:
            res.append([nums[i], nums[left], nums[right]])

            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            left += 1
            right -= 1
```

If our calculated `s` is smaller than zero, it means that we need a bigger number in the sum. To get a bigger number, we move our left pointer one step to the right. 

```Python
        elif s < 0:
            left += 1
```

If our calculated `s` is larger than zero, it means we need a smaller number. To get a smaller number, we move our right pointer one step to the left.

```Python
        else:
            right -= 1
```

Once we have scanned all combinations, we return our `res`.

```Python
return res
```

**Time Complexity**

For each index, we check all indexes to the right of it. This means that our solution has a quadratic time complexity, <code><i>O(n&sup2;)</i></code>. 

**Space Complexity**

In the worst case scenario, an array can have a quadratic number of unique triplets that sum up to zero. This would give us a total space complexity of <code><i>O(n&sup2;)</i></code>. However, looking at the auxiliary space, meaning we exclude the output, the space complexity is going to be dictated by our sorting algorithm. Pythons built in sorting uses timsort, which has a wost case sapce complexity of <code><i>O(n)</i></code>.