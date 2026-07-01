
## Explanation

**14. Longest Common Prefix**

In this problem we are given an array of strings `strs`. We are tasked to find the longest common prefix amongst the strings in the array. In this case a prefix a sequence of characters that start at index 0. In this problem the strings `flower`, `flowerbed` and `flowerpot` would have the longest common `flower`. 

Our approach to solve this problem is going to involve sorting the array. This allows us to only look at the first and last elements of the array. The reason we can do this is because the array is going to be sorted in lexicographical order. When sorting, characters from left to right is prioritized. For example if we were to sort the strings `card`, `cry` and `dog` we would look at the first letter. since `c < d` both `card` and `cry` would come before `dog`. We then look at the second letter in `card` and `cry` to determine their order. `a < r` so `card` comes before `cry`. Using this logic we know that our largest common prefix amongst all the strings in the array is going to be equal to the largest common prefix amongst the first and last strings in the sorted array.

We start by sorting the array.

```Python
strs.sort()
```

We then initialize two variables `first` and `last`. As the names suggests, they contain the first and last strings from our sorted array.

```Python
first = strs[0]
last = strs[-1]
```

We create a variable `i`, this is going to be used to store the length of the longest common prefix. We then iterate through both of the strings. If we reach the end of either of the strings or any of the letters at the same index differ the loop breaks. For each successful iteration we increment `i` by 1.  When the loop breaks we know that we have found the longest common prefix and since we have been keeping count of each successful iteration we know the length of said prefix. 

```Python
i = 0
while i < len(first) and i < len(last) and first[i] == last[i]:
    i += 1
```

We then return the first `i` characters. 


```Python
return first[:i]
```

**Time complexity**

The `.sort()` method has an average time complexity of `O(n log(n))` where `n = len(strs)`. However since we are sorting strings we have to make comparisons on a char level. The time complexity of our the sorting of our array will therefore be `O(m * n log(n))`. Our while loop has the time complexity `O(m)` where `m = max(len(strs[0]), len(strs[-1]))`. So our total time complexity will be `O(m * n log(n))` + `O(m)` =  `O(m * n log(n))`. It would be possible to reach a time complexity of O(m * n) by using a different approach, for example a vertical scan. However the performance increase would not be drastic given the constraints in the problem description. 