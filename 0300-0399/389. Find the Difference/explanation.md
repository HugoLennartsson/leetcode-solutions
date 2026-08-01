
## Explanation

**389. Find the Difference**

In this problem we are given two string `s` and `t`. String `t` is created by shuffling `s` and adding one more letter at a random position. We are tasked to find the letter that was added to `t` and return it.

Our strategy is going to involve using the `ord()` function in combination with `XOR`. We will use it the characters of both strings and store it in the same variable. We can then cancel out the characters they have in common and be left with the letter that was added.

We start by initializing our `result` variable. This is an integer variable that is going to be storing the numeric value representing the unique characters we have encountered so far.

```Python
result = 0
```

Then we start processing our string. We use `XOR` between our `result` variable and each numeric value that represents each character in our strings. We use `XOR` to eliminate each of the characters that appear in both of the strings. 

```Python
for c in s:
    result^= ord(c)
for c in t:
    result ^= ord(c)
```

When we have processed both strings we are left with the numerical representation of the added letter. Now we only need to convert it to a string. We use the `chr()` function to do that. 

```Python
return chr(result)
```

**Time Complexity**

The time complexity of this solution is <code><i>O(n + m)</i></code> where n and m are the lengths of the input strings. However since we know that the lengths between the two always differ by one, we can simplify this to <code><i>O(n)</i></code>.

**Space Complexity**

We only need to use a single integer variable for this solution. It gives us constant space complexity, <code><i>O(1)</i></code>.

