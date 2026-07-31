
## Explanation

**350. Intersection of Two Arrays II**

In this problem we are given two arrays `nums1` and `nums2`. We are tasked to return an array of their intersection. Also, each element in the result must appear as many times as they show in both arrays.

Our strategy for solving this problem is going to be sorting the arrays and then using pointers to scan through them and compare elements.

We start by sorting the arrays. We also create two pointers `i` and `j` as well as an empty array that we are going to return later.


```python
        nums1.sort()
        nums2.sort()

        i=j=0
        result = []
```

We start processing the arrays. We need to check each element in the array. We start comparing from index 0. We check if the values at those indexes match. If the values match we add the value to our result array and move both pointers forward. If they are a mismatch we move the pointer that points to the smaller value one step forward. The reason we move the smaller pointer forward is because we know that all remaining values in the other array are larger. This means that we cannot find a match for that value.

```Python
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
```

When we are done processing the array we return our result.

```Python
return result
```

**Time Complexity**

This solution requires us to sort both arrays. It also requires us to iterate through each of them, but we do it at the same time. The while loops time complexity is dictated by the larger of the two arrays. Our time complexity will be <code><i>O(n log n + m log m)</i></code> where `n` and `m` are the lengths of the input arrays. The sorting of the arrays is the limiting factor here. 

**Space Complexity**

We only use integer variables as pointers in our solution. However, the .sort() method in python uses timsort which require <code><i>O(k)</i></code> space where `k` is the length of the array that is getting sorted. Since we sort two arrays, we need <code><i>O(m + n)</i></code> space. 