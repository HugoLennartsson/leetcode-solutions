
## Explanation

**6. Zigzag Conversion**

In this problem we are given a string `s` that is written in a zig zag pattern on a given number of rows `numsRows`. We are tasked to convert the string and read it horizontally. 

We start by covering the edge cases where the number of rows is 1 or larger than the length of the string. In these cases we return the string as is `s`. 

```Python
if numRows == 1 or numRows >= len(s):
    return s 
```

After that we create an array `rows` filled with empty strings at the length of `numRows`. We also create a variable `curr_row` that we initialize to $0$. Lastly we need a boolean variable `going_down` that tells us about the direction of the zig zag. 

```Python
    rows = [''] * numRows
    curr_row = 0 
    going_down = False
```

Now we start our main loop. For each character in `s` we add that character to the index of our current row in `rows`. If our current row is in the top or bottom boundaries, we flip the direction. 

```Python
    for char in s:
        rows[curr_row] += char

        if curr_row == 0 or curr_row == numRows - 1:
            going_down = not going_down
```

After that we move up one row if we are going down, else we move up. 

```Python
    curr_row += 1 if going_down else -1
```

When we have processed each character in the string, we join our array of characters into our output string.

```Python
return ''.join(rows)
```

**Time Complexity** 

We have to iterate through the input string exactly once. This gives us a time complexity of <code><i>O(n)</i></code>.

**Space Complexity**

We have to store each character buffers across all rows before combining them. This gives us linear time complexity <code><i>O(n)</i></code>.