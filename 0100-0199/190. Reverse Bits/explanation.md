
## Explanation

**190. Reverse Bits**

In this problem we are given a 32 bit signed integer. We are tasked to reverse and return it.

We start by initializing an integer variable `res` that we are going to be building our result `integer` in.

```Python
res = 0
```

Then we start looping through each of the 32 bits. We start by left shifting `res`. This puts gives us a zero at the last bit of `res`. Since we run the loop for every bit and we want to reverse the input, we add the least significant first. Since we left shift `res` every iteration, it will therefore end up at the most significant bit once we are done.

```Python
for _ in range(32):

    res = res << 1
```


Following, we isolate the last bit in our input integer. We do this by using bitwise `AND` between our input integer and 1. This masks our input, and isolates the last bit. We start by placing the least significant bit from our input in `res` since we are moving it upwards each iteration. 

```Python
    res += (n&1)
```

When that is done, we need to prepare our input for the next iteration. We want to add the bit one step more significant. To get this done, we right shift our input. This pushes the previously least significant bit out, and replaces it with the second least significant bit. 

```Python
    n = n >> 1
```

Once we have iterated through all 32 bits, we return our reversed integer.

```python
return res
```

**Time Complexity**

This solution is tailored for a set input size, a 32 bit signed integer. Therefore it has hardcoded values for the for loop. It has constant time complexity, <code><i>O(1)</i></code>.

**Space Complexity**

We only use one integer variable `res`. Our space complexity is <code><i>O(1)</i></code>.

**Discussion**

In the problem description we are asked the following question "Follow up: If this function is called many times, how would you optimize it?". One way to do this is by trading memory for speed. You could store all possible 8-bit or 16-bit numbers and then use them on segments of the input. Another approach would be using a divide and conquer strategy. You could use a bit masking technique that works like merge sort. 