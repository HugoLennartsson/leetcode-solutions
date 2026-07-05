
## Explanation

**35. Search Insert Position** 

In this problem we are given a sorted array with distinct integers `nums` and a target value `target`. We are tasked to find the index of `target` in the `nums`. If `target` is not in `nums` we are to return the index where it would be inserted in order. The problem description also states that our solution must have a <code><i>O(log n)</i></code> runtime complexity. 

Our strategy for this problem is going to be using binary search. 

We start by initializing our `left` and `right` variables. They are our pointers for our binary search algorithm.

```Python
left = 0
right = len(nums)-1
```

Then we start processing the array. While left is **smaller or equal** to right we know that we still have not covered the entire array. We loop until this condition is broken. 

```Python
while left <= right:
```

Each iteration we find the middle point between left and right. We compare the element at the middle point with our target value. If our value is equal to the value of the element at the middle point we can simply return the middle point. 

```Python
    mid = (left + right) // 2
    if target == nums[mid]:
        return mid
```

If it is not equal there are two scenarios. Our `target` value must be smaller or greater than the value at our middle point. Since we know that the array is sorted in an ascending order, we can determine what side of the middle value our `target` value is supposed to be on. If our `target` value is smaller than our middle value, it must be placed to the `left` of the middle point. This is because we know all values to the `right` of the middle point value is greater than the value at the middle point. Therefore we move our `right` pointer to the index one step to the `left` of middle. Using similar logic, if our `target` value is greater than the value at the middle point, we move our `left` pointer to the index one step to the `right` of the middle. We keep repeating this process until we have found the `target` value or we have processed the entire array.

```Python
    elif (target > nums[mid]):
        left = mid +1
    else: 
        right = mid-1
```

If we have exited out of the loop it means that our array does not contain our `target`. In this case we are supposed to return the index that target should have been placed at. Right before the loop ends `left` and `right` will cross paths and focus on the same index. For convenience lets calls this index `mid` and the value at the index `mid_val`. The next iteration can be executed in two different ways. The first case is when `target` > `mid_val`. If this is the case we move our `left` to a greater index than `right` and our loop exits. Now `left` is pointing the spot where all elements that are smaller than `value` is to the left. The second case is when `target` < `mid_val`. If this is the case we will move our `right` to a smaller index than `left`. This will mean that `left` is pointing at the smallest number that is larger than `target`, since every index before `left` is confirmed to contain a value smaller than `target`. In both of the possible cases, the correct spot that `value` is supposed to be inserted to is `left`.

```Python
return left
```


**Time Complexity**

This solution uses binary search. The time complexity of binary search is determined by how many times you are able to split the array in half before we are left with a single element. To find the time complexity we can solve for k in the equation <code>n/2<sup>k</sup> = 1</code>. By simplifying this we get <code>n = 2<sup>k</sup></code> and further on <code>log<sub>2</sub>(n) = k</code>. This gives us a time complexity of <code><i>O(log n)</i></code>.'

**Space Complexity**

Using this approach we do not deploy any auxiliary data structures. We only use three integer variables as pointers. This means we have a space complexity of <code><i>O(1)</i></code>.