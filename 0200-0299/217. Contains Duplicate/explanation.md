
## Explanation

**217. Contains Duplicate**

In this problem we are given an integer array `nums`. We are tasked to find out if it contains any duplicate values.

Our approach is very simple. We convert `nums` to a set. We then compare the length of the set to the original array. If the length is the same, that means no duplicate elements were removed. If the length is different that means our array contains duplicates.

```python
return len(nums)>len(set(nums))
```

**Time Complexity**

To convert an array into a set, we need to iterate through each element. The len function takes constant time, so it means that our solution has a time complexity of <code><i>O(n)</i></code> where `n` is the number of elements in the array.

**Space Complexity**

We use our set as an auxiliary data structure. In the worst case it will be the size of the array. It gives us a space complexity of <code><i>O(n)</i></code>.

**Discussion**

You could optimize this solution by using a for loop and an empty set. That way the code will exit as soon as we encounter the duplicate. However, this strategy does not give us as clean and simple code. 