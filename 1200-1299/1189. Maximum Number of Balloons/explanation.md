
## Explanation

**1189. Maximum Number of Balloons**

In this problem we are tasked to find the number of times we can construct the string `balloon` with the characters in the input string `text` using each character at most once.

We start by defining a dictionary with the relevant characters we want to track. This dictionary is going to be used to track the frequency of each letter in the string `balloon`

```python
characters = {'b':0, 'a':0, 'l':0, 'o': 0, 'n': 0}
```

Then we iterate through the given string. For each character we check if it is in the keys of our characters dictionary. If it is, we add 1 to the characters corresponding value in the frequency dictionary.

```python
for char in text:
    if char in characters:
        characters[char] += 1
```

To figure out how many instances of the string `balloon` we can create we use the `min` function. We know that we need 1 `b`, 1 `a`, 2 `l`, 2 `o` , 1 `n` to create one instance. We check how many instances each character potentially could produce. Then we take the minium of that. So if we for example have enough `b` to create 10 instances, but only enough `n` to create 3 instances the function will return 3. This is what we are looking for. 

```python
return min(characters['b'], characters['a'], characters['l'] // 2, characters['o'] // 2, characters['n'])
```

This returns statement returns the maximum amount of instances we can produce by holding each character accountable. 

**Time Complexity**

Creating the dictionary and using the min function takes constant time in our problem. This is because they are unaffected by the input string. The for loop has the time complexity of <code><i>O(n)</i></code>, where `n` is the length of the input string `text`, since we iterate through each character of string one time. Therefore the time complexity of the solution is <code><i>O(n)</i></code>. 

**Space Complexity** 

In this approach, the space complexity is determined by the `characters` dictionary we use to store frequencies. We only track 5 unique characters. This means that the size of our dictionary is capped at a maximum of 5 key-value pair. This gives us a space complexity of <code><i>O(1)</i></code>.