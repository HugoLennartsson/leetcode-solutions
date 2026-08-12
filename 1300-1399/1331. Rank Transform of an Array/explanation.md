
## Explanation

**1331. Rank Transform of an Array**

In this problem we are given an array of integers `arr`. We are tasked to replace each element with its rank. Here is a quick description of how rank works from the problem description.

The rank represents how large the element is. The rank has the following rules:

- Rank is an integer starting from 1.
- The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
- Rank should be as small as possible.

We start by creating an sorted array with each unique integer. We can do this by converting `arr` to a set and then back to a list to remove duplicates. Then we just sort the array.

```Python
sorted_arr = sorted(list(set(arr)))
```

After that we create a dictionary that maps each integer value found in `arr` to its rank value. This can be a little tricky to follow so lets break it down. We use the `enumerate()` function to pair each element with its zero-based index. After that we create the key pair values. We map `num` to `i + 1`. We use `i + 1` because our enumeration uses zero-based indexing. The addition offsets all indexes by `1`, so the smallest rank will start at `1` instead of `0`.  

```Python
rank_dict = {num: i+1 for i, num in enumerate(sorted_arr)}
```

Now we have a dictionary that will let us translate each integer in `arr` to its corresponding rank. We use a list comprehension to return our new `array`. 

```Python
return [rank_dict[num] for num in arr]
```

**Time Complexity**

Our most costly operation is sorting the array. This gives our solution a time complexity of <code><i>O(n log(n))</i></code>.

**Space Complexity**

Our set, rank_dict and returned result list all uses <code><i>O(n)</i></code> space. This gives our solution a space complexity of <code><i>O(n)</i></code>.