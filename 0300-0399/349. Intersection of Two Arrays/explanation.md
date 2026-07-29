
## Explanation

**349. Intersection of Two Arrays**

In this problem we are given two integer arrays `nums1` and `nums2`. We are tasked to return an array of their intersection. The intersection of two arrays is defined as the set of elements that are present in both arrays. Each element must be unique and we are allowed to return the result in any order.

To solve this problem we convert both of our arrays to sets. We then use the AND operator between the two sets. This will give us a set of the intersection. We then convert that set to a list and return it. We can do this in a one liner.

```Python
return list(set(nums1)& set(nums2))
```

**Time Complexity**

We need to turn both of the arrays to sets so we need to iterate through each of the arrays once. Finding the intersection requires us to iterate through the smaller set and check if each element exists in the larger one. Converting the intersection to a list takes proportional time to the size of the intersection. Combining these gives <code><i>O(n + m + min(n, m) + k)</i></code>, which simplifies directly to <code><i>O(n + m)</i></code>.

**Space Complexity**

In the worst case scenario our arrays only contain unique elements, in that case our sets will be the size of our arrays and we get a space complexity of <code><i>O(n + m)</i></code>.

