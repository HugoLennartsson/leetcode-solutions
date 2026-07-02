
## Explanation

**20. Valid Parentheses**

In this problem we are given a string `s`. The string contains just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`. We are tasked to determine if if the input string is valid. It is valid if it fulfills the following criteria.

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

To solve this problem one key observation we can make is that every closing bracket must match the most recently opened bracket. We can get that behavior by using a stack. 

We start by creating a dictionary. In said dictionary we map each closing bracket to its corresponding opening bracket. We also initialize our stack.

```Python
mapping = {")" : "(", "]":"[", "}": "{"}
stack = []
```

Then we start iterating through the input string. 

```Python
for char in s:
```

The first thing we do is check weather or not the character we are currently processing is a closing bracket. If that is the case we try to pop the stack. We then check if our closing bracket matches the latest opening bracket. If it does not, we can safely return false.

```Python
    if char in mapping:
        top_element = stack.pop() if stack else "#"
        if mapping[char] != top_element:
            return False
```

If the character we are processing is an opening bracket, we simply append it to the stack and move on.

```Python
    else:
        stack.append(char)
```

When we have processed all of the characters in `s` we can determine whether or not the input string is valid by looking at the stack. If the stack is empty and we exited the loop it means that each opening bracket had a valid closing bracket. If it is not empty, it means that we have one or more open brackets that have not been closed. 

```Python
return not stack 
```

**Time Complexity**

We are iterating through the input string exactly once. All of the stack and dictionary operations we use take constant time. Therefore our solutions time complexity is `O(n)` where `n = len(s)`.