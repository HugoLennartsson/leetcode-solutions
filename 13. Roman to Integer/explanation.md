
## Explanation

**13. Roman to Integer** 

In this problem we are given a string `s` representing a roman numeral. We are tasked to convert `s` to an integer value, and return it.

We are going to be using a dictionary to convert each symbol in the roman numeral to an integer value. We are then going to be iterating through each character `s` in reverse. This solves a problem for us. Lets say we are tasked to process the numeral `CM`. If we process it in **regular** order, from left to right, we first encounter `C`. At that point, we have no idea if we should add or subtract 100 from our total. Once we move forward one step, we see that we are in fact supposed to subtract it. If we were to process it in **reverse** order we would encounter `M` first. We then simply add 1000 to our total. We then move on to the next character. We see that it is `C`. At this point we can just subtract 100 from our total without having to peak forward. The only thing we need to do is keep track of the value of our previous character.

To start, we create our dictionary.

```Python
roman_map = {
            "I": 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
            }
```

Then we initialize two variables. The variable `total` is going to be used to store the total value of the roman numeral. The variable `prev_val` is going to be used to keep track of the value of the symbol we previously processed at any given moment. This will prove useful when we have to take the `subtractive principle` in to account. 

```Python
total = 0
prev_val = 0
```

Now we process the roman numeral in reverse. For each symbol we use our dictionary to find its corresponding integer value. We then store that value in `current_value`. 

```Python
for char in reversed(s):
    current_value = roman_map[char]
```

We check if the current value we are processing is larger or equal to previously processed value. If it is, we add our current value to `total`. If our current value is larger than our previous one, it means that we adhere to the `additive principle`. Remember, we are processing the numeral in reverse.

```Python
    if current_value >= prev_val:
        total += current_value
```

If it is not, we subtract our current value from `total`. In this case we are adhering to the `subtractive principle`.

```Python
    else: 
        total -= current_value
```

We then save our current value as our previous value before we move on to the next symbol in the roman numeral.

```Python
prev_val = current_value
```

When we have processed the entire numeral we return `total`.

```Python
return total
```

**Time complexity**

We process each character in the string once. Our arithmetic operations and our dictionary indexing take constant time. Therefore the solution has the time complexity of `O(n)` where `n = len(s)`.
