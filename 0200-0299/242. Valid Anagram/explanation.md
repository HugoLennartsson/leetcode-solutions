
## Explanation

**242. Valid Anagram**

In this problem we are given two strings `s` and `t`. We are tasked to find out if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

We can start by comparing the lengths of the strings. For a string to be an anagram of another string they both must have the same length. 

```Python
if len(s) != len(t): return False
```

If the strings are the same length, it is time to check if they are anagrams of each other. This can be done by turning one of our strings into a set. We can then iterate through each character in the set and check if both our strings contain the same number of instances of that character. If the number of instances differ, they cannot be anagrams of each other. However, we know they are a perfect match if the numbers of instances do not differ, since we also know that they are the same size. 

```Python
for char in set(s):
    if s.count(char) != t.count(char): 
        return False
```

If we are able to exit the loop it means that the strings are anagrams to each other. 

```Python
return True
```

**Time Complexity**

In the worst case scenario each of the characters in our strings are unique. This makes of for loop run `n` times where `n` is the length of the string. For each iteration of the loop, we will have to iterate through both of the strings when using the `count` method. This also takes linear time. So our worst case time complexity is <code><i>O(n&sup2;)</i></code>. 

**Space Complexity**

Our space complexity is dictated by the size of our set. The set scales of the unique characters in `s`. Our space complexity is <code><i>O(k)</i></code> where `k` is the number of unique elements in `s`.

**Discussion**

This solution might seem ineffective on paper, but you have to take external circumstances into account when looking at this particular problem. If we are only using the english alphabet in lower case, our set can only grow to 26 characters. This means that we our time complexity scales to <code><i>O(n)</i></code> and our space complexity to <code><i>O(1)</i></code>. However, if we were to be implementing a solution for unicode characters we would run in to problems. There are thousands of unicode characters, there is room for over a million. Lets consider the follow up question, ```What if the inputs contain Unicode characters? How would you adapt your solution to such a case?```. A good idea would be using a frequency dictionary. You could let python do this for you, by using the `Counter` class, or creating one ourselves. This would give us a time complexity of <code><i>O(n)</i></code> and a space complexity of <code><i>O(k)</i></code>.