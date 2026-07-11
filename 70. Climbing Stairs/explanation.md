
## Explanation 

**70. Climbing Stairs**

In this problem we are given an integer `n` that represents the amount of steps it takes to climb a staircase. According to the problem description we can either climb one or two steps each time. We are tasked to return the number of distinct ways we can climb to the top. 

We are going to be using dynamic programming to solve this problem. The idea is that the number of ways to reach a step depends only on the previous two steps. Lets say we want to reach step `i`. The previous move before reaching `i` could only have been a 1 step jump from `i - 1` or a 2 step jump from `i - 2`. The number of ways to reach `i` would therefore be equal to the number of ways to reach `i - 1` plus the number of ways to reach `i - 2`. Both `i - 1` and `i - 2` could be decomposed in the same way. This pattern matches the Fibonacci sequence.

We start by handling the base case, which is when n is `1` or `2`. In these cases we can just return `n` since there is one way to reach `1` and two ways to reach `2`. 

```Python
if n <= 2:
    return n
```

Now we are going to be building the sequence explained above. We start by declaring two variables `one` and `two`. We use `one` to represent the number of ways to reach `i - 1` and `two` to represent the ways to reach `i - 2`. We start at `i = 3` since we covered `1` and `2` above when handing the base case.

```Python
one, two = 2, 1
for i in range(3, n + 1):
```

For each iteration we want to prepare `one` and `two` for the next number. The value of `one` represents the distinct ways to reach `i - 1`. To prepare it for the `i + 1` we need to update the our values so `one` and `two` represents the distinct ways to reach `i` and `i - 1` . Based on the reasoning above we know that the distinct ways to reach `i` is equal to the distinct ways to reach `i - 1` and `i - 2`. Conveniently our current `one` and `two` values represent these. We update our `one` by adding our `one` and `two` together. At this point our current `one` is correct for `i + 1`. Since our previous `one` was one step away from `i` it will be two steps away from `i + 1`. We can therefore set our new `two` to our previous `one`.

```Python
    one, two = one + two , one 
```

Our loop will exit after the iteration where `i = n`. This means that we will have prepared our `one` and `two` for `n + 1`. Our `one` will therefore contain the number of distinct ways to reach `n + 1` - `1`, which is just `n`. We return `one`.

```Python
return one 
```

**Time Complexity**

Using this method we iterate through our for loop `n - 2` times. The solution scales linearly with the integer input. Therefore our time complexity will be <code><i>O(n)</i></code>.

**Space Complexity**

We only use two integer variables to store values in this solution. The number of these are constant no matter the input. Our space complexity is therefore <code><i>O(1)</i></code>.
