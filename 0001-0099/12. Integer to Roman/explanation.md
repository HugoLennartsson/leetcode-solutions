
## Explanation 

**12. Integer to Roman**

In this problem we are given an integer and tasked to convert it to a roman number.

We start by creating a list of tuples that associates the integer value to the roman value. 

```Python
val_symbols = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]
```

After that we create an array where we are going to build the roman number. 

```Python
res = []
```

Now for our main loop. For each of the value pairs in val_symbols we find out how many times the current value fits into the number given, then we add the corresponding symbols in `res`. We start with the biggest numeral in our `val_symbols`, and try to fit as many as possible. Once `num == 0` we have found a combination of roman numerals that represents exactly the integer value,

```Python
for val, symbol in val_symbols:
      if num == 0:
        break
      count, num = divmod(num, val)
      res.append(symbol * count)
```

Once we are done we join the array and return it. 

```Python
return ''.join(res)
```

**Time Complexity**

`val_symbols` contains exactly 13 tuples, the for loop can iterate through all of these at most once. This gives us constant time complexity <code><i>O(1)</i></code>.


**Space Complexity**

Since the input has a bounded length, res will only store a bounded number of characters, small enough to treat it as constant space, O(1). 