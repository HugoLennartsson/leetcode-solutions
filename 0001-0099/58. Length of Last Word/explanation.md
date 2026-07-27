
## Explanation

**58. Length of Last Word**

In this problem we are given a string `s` that consists of words and spaces. We are tasked to return the length of the last work in the string.

We are going to be using a straight forward approach. To solve the problem we use the `.split()` method on the string to create a list with each word. Then we simply return the length of the last element in that list.

```Python
word_list = s.split()
return len(word_list[-1])
```

**Time Complexity** 

Our `.split()` method has to look at each of the characters in the string. The `len()` function constant time complexity, because it only needs to return an internal counter stored in the memory structure of the collection object it is looking at. This gives our solution a time complexity of <code><i>O(n)</i></code> where `n = len(s)`. However, by using a backward pointer it would be possible to achieve and average time complexity of O(k) where k is the length of the last word. But there is an important discussion to be had when it comes to this. Performance would be about equal when our input string follows the given constraints. When this is the case, it would be sensible to pivot towards code that is highly readable and concise. If you are in a software engineering setting this is oftentimes preferred.

**Space Complexity**

When using `.split()` we create a list with the length of the string we use it on. In this case this will give us a space complexity of <code><i>O(n)</i></code>. Using a backward pointer would grant us constant space complexity.