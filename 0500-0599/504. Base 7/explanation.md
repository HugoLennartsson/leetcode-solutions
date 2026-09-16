
## Explanation 

**504. Base 7**

In this problem we are given an integer `num`. We are tasked to return a string of its **base 7** representation.

We start of by handling the edge cases. If `num == 0` we can immediately return `"0"`. We also make a note of whether the integer is positive or negative. 

```Python
        if num == 0:
            return '0'

        is_negative = num < 0
```

After that we prepare `num` by converting it to its absolute value. This will make things easier for us down the line, and we do not lose any information since we keep track of the sign using `is_negative`. An array `digits` is created to store the base $7$ representation

```Python 
num = abs(num)
digits = []
```

Now for the main loop. Our goal is to extract the digits of the base $7$ number from right to left (least significant to most significant). We can achieve this by repeatedly dividing by $7$. Any integer $N$ in base $10$ can be written in base $7$ as: 

$$N = d_k \cdot 7^k + d_{k-1} \cdot 7^{k-1} + \dots + d_1 \cdot 7^1 + d_0 \cdot 7^0$$

Where each digit $d_i$ is between $0$ and $6$. We can see that each element is divisible by $7$, so when we calculate N mod $7$, every term containing $7$ is removed. We are left with 

$$N \bmod 7 = d_0$$

Once we have extracted the least significant digit, we use integer division by $7$ to remove it. Once we acquire this digit we convert it to a string and then add it to `digits`. The integer division will shift `num` so that the second least significant digit becomes the least significant digit. We keep doing this until we have shifted enough times to cover the whole list. 

```Python
while num > 0:
    digits.append(str(num % 7))
    num //= 7 
```

When we have processed all of `num` we use `is_negative` to check the sign of `num`. If `num` was negative, we append `"-"` to digits.

```Python
if is_negative:
    digits.append('-')
```

Since we appended to `digits` from least significant to most significant we need to reverse our array to get the correct string representation. We also need to join the array into a string.

```Python
return ''.join(reversed(digits))
```

**Time Complexity**

The time complexity of the solution is dictated by the number of digits there is in the base $7$ representation of `num`. This can be expressed as $\mathcal{O}(\log_7 \vert{}num\vert)$. Our time complexity is therefore <code><i>O(log n)</i></code> where `n = num`.

**Space Complexity**

The space complexity of the solution is also dictated by the number of digits. Therefore <code><i>O(log n)</i></code>.