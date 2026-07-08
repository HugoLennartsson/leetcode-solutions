
## Explanation

**66. Plus One**

In this problem we are given a large integer, represented as an integer array `digits`. In the array each `digits[i]` is the ith digit of the integer. We are tasked to increment the given large integer by one and then return it. 

To do this we are going to be looping through the array backwards. We know that there are two possible cases of digits we can encounter. If the current digit we encounter is a 9, and we increment it we will end up needing to increment the next digit and set our current digit to 0. If the digit we encounter is less than 9 we can simply increment it and then return the array. 

We start by creating our for loop. We want to start from the end and move forward one step at a time.

```Python
for i in range(len(digits)-1,-1,-1):
```

For each digit we check the condition `digits[i] < 9`. If the condition is met, we know we can just increment the digit and return the array.

```Python
    if digits[i] < 9:
        digits[i] += 1
        return digits
```

If the condition is not met, we know the digit we are looking at is equal to 9. In that case, we need set the digit to 0. We then move on to the next digit.

```Python
    digits[i] = 0
```

If we make it through the entire loop without returning our array, we that each digit in the input array is a 9. When this is the case we insert a 1 at the index 0. This moves all of the elements in the array one step backwards. Since we set each 9 to 0 when processing the array, we will end up with our desired number. We then return the array. 

```Python
digits.insert(0,1)
return digits
```

**Time Complexity**

The worst case time complexity occurs when each digit in the array is a 9. In cases like this we have to iterate through the entire input array, and then shift the entire array when we return it. Both of these tasks take linear time. The worst case time complexity is therefore <code><i>O(n)</i></code> where `n = len(digits)`. 

**Space Complexity**

The algorithm modifies the array in place, with the exception of the edge case where each digit is 9. The space complexity is therefore <code><i>O(1)</i></code> for all cases except the edge case. The edge case has a space complexity of <code><i>O(n)</i></code>.
