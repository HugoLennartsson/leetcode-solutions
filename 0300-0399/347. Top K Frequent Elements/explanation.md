
## Explanation

**347. Top K Frequent Elements**

In this problem we are given an array `nums` and an integer `k`. We are tasked to return the k most frequent elements in `nums`.

The main idea of the approach we are going to be using is to use the frequencies as array indices to avoid sorting the array. This way we can get a time complexity that is not limited by sorting algorithms.

We start by creating our frequency dictionary

```Python
freq = {}
```

After that we fill our frequency array. We use the .get() method to do this in a clean way. It allows us to have a default value to fall back to if we try to look up a non existent key. 

```Python
for num in nums:
    freq[num] = freq.get(num, 0) + 1
``` 

When we have our frequency array we create our buckets. The buckets are used to group the numbers by their frequency. The buckets are lists in a list. The list at index 1 contains numbers that appear once in our input array and so on. 

```Python
buckets = [[] for _ in range(len(nums) + 1)]
```

Now we need to fill our buckets. We use the rules described above. 

```Python
for num, count in freq.items():
    buckets[count].append(num)
```

We create a list for our result.

```python
res = []
```

After that we start adding our numbers to our result list, from the buckets at the highest indexes first. Every time we encounter an element in the buckets, we append it to our result list. Once our result list has `k` elements, we can return our result. 

```Python
for i in range(len(buckets) - 1, 0, -1):
    for num in buckets[i]:
        res.append(num)
        if len(res) == k:
            return res
```

**Time Complexity**

Counting the frequencies takes <code><i>O(n)</i></code> time where `n` is the number of elements in `nums`. Populating the buckets take <code><i>O(u)</i></code> time where `u` is the number of unique elements in the input array. Collecting the `k` topmost elements take in the worst case scenario `n` iterations. Based on all this our time complexity is therefore <code><i>O(n)</i></code>.

**Space Complexity**

We use O(n) space for the buckets and the frequency dictionary. Our space complexity is <code><i>O(n)</i></code>.