
## Explanation

**27. Remove Element**

In this problem we are given an array of integers `nums` and an integer `val`. We are tasked to remove all occurrences of `val` in `nums` **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)**. We are then to return the number of elements in `nums` that are not equal to `val`. The following code is used to assert our solution. 

```java
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```

The main idea of the solution will be to use a pointer to keep track of what indexes have a valid value. We start our pointer at index 0. When we encounter a value that is not equal to `val` we move it to said pointer. We then move the pointer one step to the right. This means that we can be sure that at any time, anything to the left of the pointer is not equal to `val`. Once we have processed the entire array, the pointer will carry the value representing the amount of elements we have copied.

We start by creating our pointer.

```Python
k = 0 
```

We then iterate through `nums`

```Python
for i in range(len(nums)):
```

For each value in `nums` we check if that value is not equal to `val`. 

```Python
    if nums[i] != val: 
```

If it is not, we copy that value to the index our pointer is pointing at and then move our pointer one step forward.

```Python
        nums[k] = nums[i]
        k += 1 
```

Once we have processed the entire array, we return the value of our pointer.

```Python
return k 
```

**Time Complexity**

The time complexity of the for loop is `O(n)` since we only handle each index once. The average time complexity of direct indexing in a standard python list is `O(1)`. The time complexity of the solution is therefore `O(n)`.

