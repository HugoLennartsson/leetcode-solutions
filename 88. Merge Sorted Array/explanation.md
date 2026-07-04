
## Explanation

**88. Merge Sorted Array**

In this problem we are given two integer arrays `nums1` and `nums2`. The arrays are sorted in a non-decreasing order. We are also given two integers `n` and `m`. We are tasked to merge the two arrays into a single array in a non-decreasing order. The final sorted array should be stored inside `nums1`. The length of `nums1` is `m + n` and the length of `nums2` is `n`. 

We start by creating 3 pointers. `p1` is initialized to hold the index of the last element of the subarray we want to merge from `nums1`. p2 is initialized to hold the index of the last element of the subarray we want to merge from `nums2`. `p_merge` is initialized to hold the index of the last element of the expected merged subarray. 

```Python
p1, p2, p_merge = m - 1, n - 1, m + n - 1
```

While both p1 and p2 are greater or equal to zero, we check what value is greater between *the value in `nums1` that `p1` is pointing to* and *the value in `nums2` that `p2` is pointing to*. The greatest value of those two is written to the index our `p_merge` pointer is pointing at. The pointer corresponding to the value that has been written is then decremented as well as our `p_merge` pointer.

```Python 
    while p1>=0 and p2 >=0:
        if nums1[p1] > nums2[p2]:
            nums1[p_merge] = nums1[p1] 
            p1 -= 1
        else:
            nums1[p_merge] = nums2[p2]
            p2 -=1 
        p_merge -= 1 
``` 

The while loop above can exit in two ways. Scenario 1 is that `p1` reaches `0` before `p2`. In this case we will need to copy the remaining elements from `p2` to the front of `p1`. Scenario 2 is that `p2` reaches `0` before `p1`. If this is the case we know that the remaining elements are already in `nums1` in the right place. Therefore we will only need to cover scenario 1. 

```Python
    while p2>=0:
        nums1[p_merge] = nums2[p2]
        p2 -= 1
        p_merge -=1
```

At this point we can be sure that the first `m + n` elements of the array is sorted. 

**Time complexity**

Our while loops are guaranteed to run exactly `m + n` times. Therefore it can be concluded that the time complexity of the solution is <code><i>O(m + n)</i></code>.
