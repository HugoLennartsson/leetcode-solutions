
## Explanation

**10. Regular Expression Matching**

In this problem we are given an input string `s` and a pattern `p`. We are tasked to implement a regular 
expression matching with support for `'.'` and `'*'` where:
- `'.'` Matches any single character.​​​​
- `'*'` Matches zero or more of the preceding element.

We are to return a boolean indicating whether the matching covers the entire input string.

We start by initializing two variables to keep track of the length of `s` and `p`.

```Python
m, n = len(s), len(p)
```

After that we create a 2D array `dp` containing lists filled entirely by `False`. Conceptually, the list stores a boolean flag that answers the question "Does the first `i` characters of the string `s` match the first `j` characters of pattern `p`?".

```Python
dp = [[False] * (n + 1) for _ in range(m + 1)]
```

Now, we handle the base case. The first 0 characters in `s` will match the first 0 characters in `j`.

```Python
dp[0][0] = True
```

Following, we handle the base case for when `s` is an empty string. We handle this in a two step process. First we check if the current character in the pattern is `*`. If it is, it can match zero occurrences of the preceding character. Therefore, the `*` and the preceding character cancel out. This means that the match status for the pattern up to index `j` inherits whatever the status was two positions back, since we ignore both the `*` and the character before.

```Python
for j in range(2, n + 1):
    if p[j - 1] == '*':
        dp[0][j] = dp[0][j - 2]
```

Now for our main loop. We have a nested loop that fills the rest of the DP array by comparing every prefix of `s` against every prefix of `p`. 

```Python
for i in range(1, m + 1):
    for j in range(1, n + 1):
```

We break it down into two branches. The first branch is if we encounter a `*`. In this case we can break it down into two possibilities. If either of the possibilities is `True`, `dp[i][j]` becomes `True`.


```Python
    if p[j - 1] == '*':
```

Possibility one is that we ignore the `*` and its preceding character at `p[j - 2]` like in the base case. Here, we inherit the status two positions back. 

```Python
        dp[i][j] = dp[i][j - 2]
```

The second possibility is when there is one or more occurrences. This would be if the character preceding `*` matches the current string character `s[i - 1]` or if the current string is `'.'`. If this is the case the validity will be decided by if possibility one was already true or if we are able to consume the current character from `s`, and keep `*` available to consume more characters later. 

```Python
        if p[j - 2] == '.' or p[j -2] == s[i - 1]:
            dp[i][j] = dp[i][j] or dp[i - 1][j]
```

Let the following example illustrate it. Consider `s = "aaa"` and p = `"a*"`. Supposed we are at `i = 3` and `j = 2`. Lets check possibility one first where a `*` lets us ignore it and its preceding character. Does `"aaa"` match `""`? It does not, so we move on and check for the second possibility. Here we check if the one character shorter version `"aa"` matches our pattern `"a*"`. Our previous step at `dp[2][2]` already determined if they match, so we take its result. In this case they matched so `dp[3][2]` is `True`.

Now we need to break down the other branch, where we do not encounter a `*` but instead a `.` or a character. In this case we check if our current character is a `.`, meaning its a wildcard, or if our current character in the pattern matches the current character in the string. Since the current characters match the overall status for the current prefixes depends on whether the previous prefixes has matched.

```Python
    else:
        if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
            dp[i][j] = dp[i - 1][j - 1]
```

When we have processed the combinations of the strings, we return `dp[m][n]`. This tells us if the full string of length m matches the full pattern of length n. 

```python
return dp[m][n]
```

**Time Complexity**

We use a nestled for loop, giving us a time complexity of <code><i>O(n&times;m)</i></code>. However the string lengths are capped at 20 characters, meaning that it can run for a maximum of 400 iterations.

**Space Complexity**

We use a 2x2 matrix for this solution, giving us a space complexity of <code><i>O(n&times;m)</i></code>. This can be optimized by only keeping two 1D rows in memory during execution.

