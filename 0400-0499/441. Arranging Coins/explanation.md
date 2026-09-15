
## Explanation 

**441. Arranging Coins**

In this problem we are given an integer `n` that represent a number of coins. We can use the coins to build a staircase of `k` rows where the ith row has exactly `i` coins. We are tasked to find and return the number of complete rows of the staircase we can build. 

Building `k` complete rows requires a total number of coins equal to the sum of the first `k` integers. This can be described as 

$$\text{Total Coins} = \frac{k(k + 1)}{2}$$. 

Our number of coins available is `n`. To find how many complete rows we can create we can setup this formula 

$$\frac{k(k + 1)}{2} \le n \implies k^2 + k - 2n \le 0$$. 

Now we solve the equation using the quadratic formula. 

$$k = \frac{-1 + \sqrt{1 + 8n}}{2}$$

```Python
return int((math.sqrt(1 + 8 * n) - 1) // 2)
```

**Time Complexity**

We only use arithmetic operations in our solution, our time complexity is <code><i>O(1)</i></code>.

**Space Complexity**

We do not use any auxiliary variables, the space complexity is <code><i>O(1)</i></code>.