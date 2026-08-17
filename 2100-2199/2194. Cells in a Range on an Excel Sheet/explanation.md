
## Explanation

**2194. Cells in a Range on an Excel Sheet**

In this problem we are given a string `s` in the format `<col1><row1>:<col2><row2>` where `<col1>` represents the column `c1`, `<row1>` represents the row r1, `<col2>` represents the column `c2`, and `<row2>` represents the row `r2`, such that `r1 <= r2` and `c1 <= c2`. We are tasked to return the list of cells such that `r1 <= x <= r2` and `c1 <= y <= c2`. See the problem description for clarification on the problem.

We start by creating the list that we are going to be returning. 

```Python
return_list = list()
```

Now we need to build the cells from the information provided in `s`. We create a nested for loop where the outer loop handles columns and the inner one handles rows. 

To iterate through the range of cells provided we convert the characters to their numeric representation. 

```Python
for uni in range(ord(s[0]), ord(s[-2]) + 1):
```

To iterate through the rows we simply need to convert parts of the input string to integer values. 

```Python
    for num in range(int(s[1]), int(s[-1]) + 1):
```

After that we can simply construct each (column, row) pair and append it to our return list. 

```Python
        cell = chr(uni) + str(num)
        return_list.append(cell)
```

When we have processed the entire range described by `s` we return our list.

```Python
return return_list
```

**Time Complexity**

If we look at the constraints in the problem description we see that possible cells `A` through `Z` and possible rows are single digits. This gives us a maximum of 234 iterations regardless of input. This means that our time complexity is constant, <code><i>O(1)</i></code>.

**Space Complexity**

We use scalar variables. These require constant auxiliary space, <code><i>O(1)</i></code>.


