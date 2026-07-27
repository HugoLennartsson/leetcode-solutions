
## Explanation

**1. Two Sum**

In this problem we are given an array of integers and an integer target. We are asked to return two indices that contains two numbers that add up to the target. We are also told that each input has **exactly one** solution.

Our approach is going to be using a dictionary where each index in the given array is stored as a value. The key to each value is going to be the difference between our target value and the integer value of that index in the input array. For example, if we have target `7` and want to store index `1` that contains value `2` in the dictionary we will end up with key-pair value `dict[5] = 1`. The reason we use this approach is because a dictionary has an time complexity `O(1)` for key lookups. This means that for each index in the given array we are able to calculate what value the other pair needs to be in order to reach the target value. And since we store the index as the value, we are also able to find it without trouble. 

We create our dictionary.

```python
num_dict = dict()
```

Then, for each index in `nums` we check if the value of that index is a match for another value in the input array, that we have already stored in the dictionary. If it is we return the index pair of the two values. 

```python
for i in range(len(nums)):
    if nums[i] in num_dict:
        return [num_dict[nums[i]], i]
```

If it is not, we add the value that needs to be added to our current value in order to reach the target as key, and the index of the current value as value to the dictionary. 

```python
    else: num_dict[target - nums[i]] = i 
```

**Time Complexity**

In this problem we are iterating through the input array a maximum of `1` time. All of our dictionary operations take on average constant time, <code><i>O(1)</i></code>. This means that the overall time complexity of the solution is <code><i>O(n)</i></code>. 

**Space Complexity** 
Since we utilize an auxiliary dictionary `num_dict` to store the complements of the numbers we have visited so far we can determine that in a worst case scenario we will have to store `n - 1`. So we get an average space complexity of <code><i>O(n)</i></code>. If we wanted to minimize our space complexity we could make a tradeoff and use brute force to solve the problem. This would give us a space complexity of <code><i>O(1)</i></code> but it would make our time complexity <code><i>O(n&sup2;)</i></code>.