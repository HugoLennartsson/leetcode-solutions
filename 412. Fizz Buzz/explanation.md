
## Explanation

**412. Fizz Buzz**

In this problem we are given an integer `n`. We are then tasked to return as string array `answer`. Answer should fulfill the following criteria:

* `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5.
* `answer[i] == "Fizz"` if `i` is divisible by 3.
* `answer[i] == "Buzz"` if `i` is divisible by 5.
* `answer[i] == i` (as a string) if none of the above conditions are true.

We start by creating our `answer` array. 

```python
answer = []
```

Then we iterate from `0` to `n`. 

```Python
for num in range(1,n+1):
```

For each number we check our conditions listed above. 

If `num` is divisible by 3 and 5 we append `"FizzBuzz"` to `answer`.

```Python 
    if num % 3 == 0 and num % 5 == 0:
        answer.append("FizzBuzz")
```

If it is divisible by 3, but not 5 we append `"Fizz"` to `answer`.

```Python
    elif num % 3 == 0:
        answer.append("Fizz")
```

If it is divisible by 5, but not 3 we append `"Buzz"` to `answer`.

```Python
    elif num % 5 == 0:
        answer.append("Buzz")
```

If it is neither divisible by 5 or 3 we append `num` to `answer`

```Python
    else: answer.append(str(num)) 
```

Once we have handled every num between `0` and `n` we return `answer`.

```Python
    return answer
```

**Time Complexity**

We pass through the each integer from `0` to `n` in the for loop. Therefore the time complexity will be <code><i>O(n)</i></code>. 