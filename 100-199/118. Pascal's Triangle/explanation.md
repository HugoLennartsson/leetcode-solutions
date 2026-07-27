
## Explanation

**118. Pascal's Triangle**

In this problem we are given an integer `numRows`. We are tasked to return the first `numRows` of <a href="https://en.wikipedia.org/wiki/Pascal%27s_triangle">Pascal`s triangle</a></a>. 

We start by initializing an empty list for our triangle. 

```Python
triangle = []
```

Then we start constructing the rows in the triangle, one by one. We fill each row with `1`. Then for each element except the first and last one in the row, we calculate its value by looking at the two values above the current position. We then add the row to our list. 

```Python
    for i in range(numRows):
        row = [1] * (i+1)

        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
```

When we have constructed our triangle we simply return it. 

```Python
return triangle
```

**Time Complexity** 

The outer loop runs `n` times, where `n = numRows`. The inner loop runs proportional to the size of the row it is processing. This forms the arithmetic progression <code><i>1 + 2 + 3 + ... + n = n(n + 1)/2</i></code>. This gives us a time complexity of <code><i>O(n&sup2;)</i></code>.

**Space Complexity**

The auxiliary space complexity is <code><i>O(n)</i></code>. This is because the largest temporary row we allocate is of size n. If you account for the final output matrix the space complexity is <code><i>O(n&sup2;)</i></code>.