
## Explanation

**3. Longest Substring Without Repeating Characters**

In this problem we are given a string `s`. Our task is to find and return the longest substring without duplicate characters in `s`.

We start by creating a dictionary for mapping characters to positions in the array. We create a variable `left` that we use to represent the leftmost part of a substring. Lastly we need a variable to keep track of the length of the longest substring we have encountered so far, we call it `max_length`. 

```Python
char_map = {}
left = 0 
max_length = 0 
```

Now for the main loop. We use the enumerate function to associate each character with its index. 

```Python
for right, char in enumerate(s):
```

We check if each character we encountered is already in our `char_map`. If it is in our `char_map` and the index associated with the character is larger than the leftmost index of our substring it means that our current substring will become invalid if we add said character. This is our current character is a duplicate. In this case we move our left pointer one step past the last index we encountered our current character. 

```Python
if char in char_map and char_map[char] >= left:
    left = char_map[char] + 1
```

Regardless if we have encountered our current char before or not, we add or update the value of the character in `char_map` and set it to `right`. In the end of each iteration we check if our current substring is larger than our `max_length`. If it is we update the `max_length` value to the length of our substring, otherwise we keep our old `max_length`.

```Python
    char_map[char] = right 
    max_length = max(max_length, right - left + 1)
```

Once we have processed the entire string we return our `max_length`.

```Python
return max_length
```

**Time Complexity**

We iterate through the input string once, we get a time complexity of <code><i>O(n)</i></code> where `n` is the length of `s`

**Space Complexity**

The space complexity is dictated by how many characters there is in `char_map`. Since it only holds unique characters we can formulate the space complexity as O(m) where `m` is the number of unique characters in `s`. If we have a fixed character set we can view the space complexity 
