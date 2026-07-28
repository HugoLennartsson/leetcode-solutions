
## Explanation

**202. Happy Number**

In this problem we are given a number `n`. We are tasked to figure out if the number is a happy number. See the problem description if you are unsure what a happy number is.

We start by creating a set that we used to store information about the sums we have seen. This is because if we encounter a number that we have already encountered, we know that we will be stuck in a loop where we keep coming back to that number.

```Python
seen = set()
```

Now we start iterating through our while loop. We want to keep iterating until our sum becomes one, or until we find an sum that we have already encountered.

```python
while n != 1:
    if n in seen:
        return False
```

Every iteration we add `n` to `seen`, so that we can recognize if we have gotten stuck in a cycle. 

```Python
    seen.add(n)
```

We then calculate the sum of the square of the digits of `n`. To do this we turn `n` into a string, and then iterate through each of the digits, turing each digit back into an integer and the squaring it. We sum all of the squares of the digits this way.

```Python
    n = sum(int(d)**2 for d in str(n))
```

If we make it out of the loop, it means that we have gotten to a point where `n = 1`. In that case we return `True`.

**Time Complexity**

It is not very straight forward to figure out the time complexity of this problem. Firstly we can look at how long it takes to process one number. For each `n` we need to convert it to a string. This forces us to iterate through the digits of the number. It takes `log n` iterations to do this. Now we can look at how many times we need to run the loop. For any number in the range 1 <= n <= $2^{31} - 1$ it would only take a few iterations to get the number to drop under 243. At that point there is only a finite amount of numbers left to land on. This means that there is a negligible number of iterations needed to shrink the number until there is a loop or it hits zero. Our final time complexity is therefore <code><i>O(log n)</i></code>.


**Space Complexity**

This is determined by how big the set `seen` is. The number of elements added to the set before the value drops below 243 is proportional to the number of digits in the original number. This gives us a space complexity of <code><i>O(log n)</i></code>. 

**Discussion**

There is an optimization that can be done to this solution, provided that you know the math behind the sum of squared digits for numbers with the base 10. Every single unhappy number will get stuck in the same 8-number sequence. The sequence is the following
 $$\mathbf{4 \rightarrow 16 \rightarrow 37 \rightarrow 58 \rightarrow 89 \rightarrow 145 \rightarrow 42 \rightarrow 20 \rightarrow 4} ...$$
Knowing this, we are able to create a set that has a constant memory size. We also don't need to iterate through the entire sequence to find out that our number is unhappy. We simply look for the numbers in the sequence.
