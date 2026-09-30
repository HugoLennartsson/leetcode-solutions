
## Explanation

**7. Reverse Integer**

In this problem we are given a signed 32-bit integer `x`. We are tasked to return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2³¹, 2³¹ - 1]`, then return $0$. We are also to assume that our environment cannot store 64-bit integers.

We start by initializing two variables that represent the end points of our valid interval for values of `x`. 

```Python
MAX_INT = 2**31 -1 
MIN_INT = -2**31
```

We also create a variable `rev` to build and store our reversed integer in. 

```Python
rev = 0
```

Now we start reversing the string. Each iteration of our loop we extract the last digit of x using the `fmod` method. We do this instead of using the modulo operator built in to python since it rounds towards negative infinity. This means that `-123 % 10 = 7` but `math.fmod(-123, 10)` returns $-3$. The `fmod` method will return a float, so we convert it to an int. 

```Python
while x != 0:
    pop = math.fmod(x,10)
    pop = int(pop)
```

After that we need to shift the digits so that the second least significant digit is at the least significant spot. We do this by dividing the number by 10, and then converting it to an integer to remove any decimals. 

```Python
    x = int(x / 10)
```

Now we check if our reversed integer is out of the valid interval. 

```Python
    if rev > MAX_INT // 10 or (rev == MAX_INT // 10 and pop > 7):
        return 0
    if rev < math.ceil(MIN_INT / 10) or (rev == math.ceil(MIN_INT / 10) and pop < -8):
        return 0 
```

After that we add our digit to `rev`.

```Python
    rev = rev * 10 + pop
```

When we exit our loop we return `rev`

```Python
return rev
```

**Time Complexity**

The time complexity depends on the number of digits in `x`. This gives us <code><i>O(log n)</i></code> where n is the number of digits in `x`.

**Space Complexity**

We use the same amount of memory regardless of input size, this gives us <code><i>O(1)</i></code>.