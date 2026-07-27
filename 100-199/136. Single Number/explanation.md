
## Explanation

**136. Single Number**

In this problem we are given an integer array `nums`. We are told that the array contains duplicate elements with the exception of one. Our task is to find that element by implementing a solution that with linear runtime complexity and constant auxiliary space. 

To solve this, we are going to be using XOR. There are two properties that makes XOR fit for our case. Firstly, if we use XOR with a number and zero, the result will be the number. If we use XOR with two of the same number we will get zero. This means that if we start with zero, all of the duplicates will cancel each other out and we will be left with our exception element.

We start by initializing an integer `result` to 0. We will use this to store the results of our XOR operations.

```Python
result = 0
```

We then iterate through our `nums` array. For each element we use the XOR operation with our `result` variable.

```Python
for num in nums:
    result ^= num
```

When we have iterated through all of the elements in the array, we know our XOR operation has canceled out all of the duplicates. We are then left with the exception element.

**Time Complexity**

We iterate through the array once. This gives us a time complexity of <code><i>O(n)</i></code> where `n` is the number of elements in `nums`.

**Space Complexity**

The only thing we store in memory during runtime is integer variable `result`. This gives us an auxiliary time complexity of <code><i>O(1)</i></code>.