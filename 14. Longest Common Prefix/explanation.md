
## Explanation

**14. Longest Common Prefix**

In this problem we are given an array of strings `strs`. We are tasked to find the longest common prefix amongst the strings in the array. In this case a prefix a sequence of characters that start at index 0. In this problem the strings `flower`, `flowerbed` and `flowerpot` would have the longest common `flower`. 

Our approach to solve this problem is going to involve sorting the array. This allows us to only look at the first and last elements of the array. The reason we can do this is because the array is going to be sorted in lexicographical order. When sorting, characters from left to right is prioritized. For example, if we were to sort the strings `card`, `cry` and `dog` we would start by looking at the first letter. Since `c < d`, both `card` and `cry` would come before `dog`. We then look at the second letter in `card` and `cry` to determine their order. Because `a < r`, `card` comes before `cry`. Knowing this we can determine that the largest common prefix amongst all the strings in the array is the same as the largest common prefix between strings with the smallest and largest lexicographical values. Conveniently these are going to be the first and last elements of the sorted array.

We start by sorting the array.

```Python
strs.sort()
```

We then initialize two variables `first` and `last`. As the names suggests, they contain the first and last strings from our sorted array.

```Python
first = strs[0]
last = strs[-1]
```

We create a variable `i`. The variable is going to be used to store the length of the longest common prefix. We then iterate through both of the strings. If we reach the end of either of the strings or if we find letters at the same index that differ, the loop breaks. For each successful iteration we increment `i` by 1.  When the loop breaks we know that we have found the longest common prefix and since we have been keeping count of each successful iteration we know the length of said prefix. 

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

The `.sort()` method has an average time complexity of `O(n log(n))` where `n = len(strs)`. However, since we are sorting strings we have to make comparisons on a char level. The time complexity of our the sorting of our array will therefore be <code><i>O(m &middot; n log(n))</i></code> where m is the length of the longest string in `strs`. Our while loop has the time complexity <code><i>O(m)</i></code>. So our total time complexity will be <code><i>O(m &middot; n log(n))</i></code> + <code><i>O(m)</i></code> =  <code><i>O(m &middot; n log(n))</i></code>. It would be possible to reach a time complexity of <code><i>O(m &middot; n)</i></code> by using a different approach, for example a vertical scan. However the performance increase would not be drastic given the constraints in the problem description. 