
## Explanation

**8. String to Integer (atoi)**

In this problem we are tasked to implement a function `myAtoi(string s)` that converts a string to a 32-bit signed integer. The algorithm is explained as following. 

1. **Whitespace**: Ignore any leading whitespace (" ").
2. **Signedness**: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
3. **Conversion**: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is $0$.
4. **Rounding**: If the integer is out of the 32-bit signed integer range [$-231$, $231$ - $1$], then round the integer to remain in the range. Specifically, integers less than $-231$ should be rounded to $-231$, and integers greater than $231$ - $1$ should be rounded to $231$ - $1$.

We start by defining two variables that are the edges of our accepted integer values. We also initialize two variables, `n` to keep track of our input string length and `i` to keep track of the index in the string we are looking at.

```Python
INT_MAX = 2**31 -1
INT_MIN = -2**31

n = len(s)
i = 0
```

Now we start with the first step of the algorithm, we ignore any leading whitespaces. 

```Python
while i < n and s[i] == ' ':
    i += 1
```

After we have skipped all leading whitespaces we check if we have reached the end of the string, meaning that the string only consisted of whitespaces. In that case we return $0$.

```Python
if i == n:
    return 0
```

Now we move on to step two in the algorithm. We need to check for a sign. We start by initializing a variable `sign`. If we find a subtraction sign we set our `sign` variable to $-1$. We then move on to the next index.

```Python
sign = 1
if s[i] == '-':
    sign = -1
    i += 1
elif s[i] == '+': 
    i += 1
```

After that we move on to step 3 of the algorithm. We calculate each digit as an integer by subtracting its numerical representation by the numerical representation of `'0'`. Then we add it as the last digit in our `res` variable. When we are done processing the integer, we multiply it by the sign we found earlier.

```Python
while i < n and s[i].isdigit():
    digit = ord(s[i]) - ord('0')
    res = res * 10 + digit
    i += 1
res = sign * res
```

The final step is to check for the rounding. 

```Python
if res < INT_MIN:
    return INT_MIN
if res > INT_MAX:
    return INT_MAX
```

After that we just return our `res`.

```Python
return res
```

**Time Complexity**

The maximum number of iterations is the length of the string. This gives us a time complexity of <code><i>O(n)</i></code>.

**Space Complexity**

We only used scalar variables for this solution. We get constant space <code><i>O(1)</i></code>.