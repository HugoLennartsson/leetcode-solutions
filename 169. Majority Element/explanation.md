
## Explanation

**169. Majority Element**

In this problem we are given an array `nums` of size `n`. We are tasked to return the majority element. It is also mentioned that our solution should have linear runtime complexity and use constant space. We are also told that there will always be a majority element in the `nums`.

We are going to be constructing a solution that uses the <a href="https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm">Boyer-Moore majority vote algorithm</a>. Simply put, this algorithm finds the majority element in a sequence of elements using a voting system where each element casts a vote. 

We start by initializing two variables `candidate` and `count`. Our `candidate` is going to be used to keep track of what element we have encountered the most of at any time when we are iterating through the array. We use `count` to keep track of how many more of our `candidate` elements we have encountered opposed to the other elements.

```Python
candidate = None
count = 0
```

Now we start iterating through `nums`. If count is `0` it means that we have just started iterating or that our previous `candidate` has just been canceled out by other numbers. In that case, we just set our current element to as `candidate` since the playing field is balanced. If our number encountered matches the `candidate`, we it casts a vote by incrementing `count`. If it does not match `candidate` it casts a vote against `candidate` by incrementing `count`. The majority element will have the most votes to cast, and since it always votes against other candidates or for it self, `candidate` will always end up representing the majority element after we have iterated through the array. 

```Python
for num in nums:
    if count == 0:
        candidate = num
    count += 1 if num == candidate else -1
```

When we have iterated through the array, we return `candidate`.

```Python
return candidate
```

**Time Complexity**

This solution requires us to iterate through the input array once. It gives us a time complexity of <code><i>O(n)</i></code>.

**Space Complexity**

This solution only makes use of two auxiliary variables, no matter what the input size is. This gives us a space complexity of <code><i>O(1)</i></code>.