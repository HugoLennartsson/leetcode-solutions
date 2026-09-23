
## Explanation

**4. Median of Two Sorted Arrays**

In this problem we are given two sorted arrays `nums1` and `nums2`. We are tasked to return the median of the two sorted arrays using an algorithm that has an overall run time complexity of <code><i>O(log(m + n))</i></code> where m and n are the lengths of `nums1` and `nums2`.

It might feel intuitive to create a solution by merging the two arrays then taking the middle index, however this would require us to iterate through each element of both arrays once. A better solution would be partitioning the arrays. The median spits the dataset into two halves. We want to find a partition line that in `nums1` at index `i` and `nums2` at index `j` where the sum of the elements to the left of `i` in `nums1` and `j` in `nums2` is equal to the number of elements to the left of the median. It can be mathematically explained like the following. 

$$i + j = \frac{m + n + 1}{2}$$

Our partition will be valid if all numbers to the left of `i` in `nums1` are less or equal to the value at `j` and vice verse. This could be described as the following.

$$\text{nums1}[i-1] \le \text{nums2}[j] \quad \text{and} \quad \text{nums2}[j-1] \le \text{nums1}[i]$$

Now, lets get started with the solution. We are going to use binary search in order to find a valid partition. Since i and j are dependant of each other in the formula above, we only need to run binary search on one of the arrays. However, if we choose to use the larger array we risk choosing an extreme value that would calculate and index that falls outside of the range of the smaller array. Also, choosing to run binary search on the smaller array will give us a better time complexity than running it on the larger or both of the arrays. We make sure that `nums1` is the smaller array.

```Python
if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1
```

Then we initialize our variables we are going to be using. We use `m` and `n` to keep track of the lengths of the arrays. Our pointers for binary search are `low` and `high`. We can also calculate the index of the median. 

```Python
m, n = len(nums1), len(nums2)
low, high = 0, m
half_len = (m + n + 1) // 2
```

When we have that set up we can start our main loop. Each iteration we use binary search to try to find and `i` and `j` that fulfills the following.

$$\text{nums1}[i-1] \le \text{nums2}[j] \quad \text{and} \quad \text{nums2}[j-1] \le \text{nums1}[i]$$

We set `i` to the midpoint of our current window, and `j` as `half_len - i`. 

```Python
while low <= high:
    i = (low + high) // 2 
    j = half_len - i 
```

Now we simply need to calculate the parts of the requirements above. 

```Python
    max_left1 = float('-inf') if i == 0 else nums1[i - 1]
    min_right1 = float('inf') if i == m else nums1[i]

    max_left2 = float('-inf') if j == 0 else nums2[j - 1]
    min_right2 = float('inf') if j == n else nums2[j]
```

Now we check if our partition is valid.

```Python
    if max_left1 <= min_right2 and max_left2 <= min_right1: 
```

If our partition is valid we have found the median. However, we need to take into account if our total number of elements are even or odd. If the number of elements are odd, we can return the middle element. When calculating `half_len` previously we intentionally gave one extra element to the left. That means that the median will of the combined arrays if the length is odd is the largest element in the left hand part.

```Python
        if (m + n) % 2 == 1:
            return float(max(max_left1, max_left2)) 
```

If the total number of elements is even we need to find the largest value in the left part and the smallest value in the right part, add them, and then divide the sum by $2.0$. 

```Python
        return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
```

If our partition is not valid, we keep on searching. If the value at `nums1[i - 1]` is larger than at `nums2[j]` we are taking too many elements from `nums1` into the partition. In this case we rule out any element that is at index `i` or higher. 

```Python
    elif max_left1 > min_right2:
        high = i - 1
```

If we are not taking too many elements, but still do not have a valid partition it means we are not taking enough elements from `nums1`. This could be formulated as taking to many elements from `nums2`. We shrink `nums2` by increasing our lower boundary of the binary range past `i`. 

``` Python
    else:
        low = i + 1
```

In order to keep static type checkers happy, we return a float value outside of the loop. However, it is guaranteed based on the constraints that the merged array will have a median value. 

**Time Complexity**

We are using binary search on the smaller array. This gives us a time complexity of <code><i>O(log(min(m,n)))</i></code> where `m` and `n` are the lengths of the arrays.

**Space Complexity**

We operate in place and only make use of a set number of scalar variables, our space complexity is <code><i>O(1)</i></code>