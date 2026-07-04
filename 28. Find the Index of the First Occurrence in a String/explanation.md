
## Explanation

**28. Find the Index of the First Occurrence in a String**

In this problem we are given two strings `needle` and `haystack`. We are tasked to return the index of the first occurrence of `needle` in `haystack`. If there is no occurrence we are to return `-1`.

Our strategy is going to be checking each substring with the same length as our `needle` in our `haystack`, starting from the first character. 

We start by declaring two variables `m` and `n` which represent the length of our `haystack` and `needle`.

```Python
n, m = len(haystack), len(needle)
```

Then we iterate through `haystack`. For each index we check if the substring that starts on that index and has the length of our `needle`, is equal to our `needle` string. If it is we return that index. If we have fully processed `haystack` and still not found the `needle`, we know that needle is not in `haystack`. In that case we return `-1`. 

```Python
for i in range (n-m + 1):
    if haystack[i:i+m] == needle:
        return i
return -1
```

**Time complexity**

In this solution we iterate through our for loop `n - m + 1` times. During each iteration we slice our haystack string to a substring of size `m` and compare it character by character to `needle`. Our combined time complexity will be <code><i>O((n - m) &middot; m)</i></code> which can be simplified to <code><i>O(n &middot; m)</i></code>. You are able to achieve a time complexity of <code><i>O(n)</i></code> if you can use pointers instead of slicing. This however, will not have a large effect on runtime since `m` and `n` are so small. 