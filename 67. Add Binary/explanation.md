
## Explanation

**67. Add Binary**

In this problem we are given two binary strings `a` and `b`. We are tasked to return their sum as a binary string.

Our strategy is going to involve processing the binary strings backwards. Essentially we are trying to figure out how to do binary addition using code instead of doing it on paper. We think of the problem as a translation problem. We know how to do a task on paper, now we want to translate that method to a program. 

When we are adding binary numbers we start from the least significant digit, so we do the same in our program. We also know that if we add two ones we are going to need a carry. We create a variable to keep track of that carry. We also create a res array that we are going to use to create our binary string.

```Python
res = []
carry = 0
i, j = len(a) -1, len(b) -1 
```

We are going to be looping from the least significant digit to the most significant digit in both of our strings. We do not stop until both strings have been looped through and our carry flag is zero. 

```Python
while i >= 0 or j >= 0 or carry: 
```

At the start of the loop we get both of the digits for the index in the string we are looking at. We know that we can freely add zeros at the start of our binary number while still keeping the same value. Therefore, if we have already reached the end of the string we are getting the digit from we can just use zero. 

```Python
    digit_a = int(a[i]) if i >=0 else 0
    digit_b = int(b[j]) if j >=0 else 0
```

After this we add our `digit_a`, `digit_b` and `carry`. There are three possible results from this. If our `total` becomes zero or one, we can simply add it to our `res`. If the result is two or three we need to set our carry flag and then return zero or one. There is a clear pattern here though. Zero and two calls for returning zero. One and three calls for returning one. We can therefore use the modulo operator to find out what we should add to our `res` array.

```Python
    total = digit_a + digit_b + carry
    char = str(total % 2)
    res.append(char)
```

When we have done that we need to decide if we are going to set our carry flag. We want to set it when total is two or three. If it is zero or one we want it not to be set. To solve this we can simply use integer division by two. This gives us the result we are looking for. 

```Python
    carry = total // 2
```

Then we simply move our pointers to the next digit.

```Python
    i -= 1
    j -= 1 
```

Now all we need to do is turn our `res` array into a string. We use the `.join()` method. Since we added our digits to the start of the array, our representation of the binary string is reversed. To solve this problem we use `[::-1]` when we slice our list. The syntax for slicing is `[start:stops:step]`. By leaving the `start` and `stop` empty but setting `step` to negative one we can reverse the list. 

```Python
return ''.join(res[::-1])
```

**Time Complexity**

In our solution the while loop will run until both lists have been iterated through and the carry flag is set to zero. This means that the maximum amount of iterations possible for the loop is equal to the longest of the binary strings plus one. The plus one comes from the final iteration when the carry flag is set. So our loop has a time complexity of <code><i>O(max(n, m) + 1)</i></code> = <code><i>O(max(n, m))</i></code> where `m = len(a)` and `n = len(b)`. To reverse our list we need to traverse it once, the list will in be max(n, m) long. The list reversal has the time complexity <code><i>O(max(n, m))</i></code>. This means the solution has a time complexity of <code><i>O(max(n, m))</i></code>.

**Space Complexity**

We use a list `res` as our auxiliary data structure. This list scales with the `max(m, n)`. Our space complexity is therefore <code><i>O(max(n, m))</i></code>.