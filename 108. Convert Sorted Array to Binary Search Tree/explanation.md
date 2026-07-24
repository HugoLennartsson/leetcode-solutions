
## Explanation

**108. Convert Sorted Array to Binary Search Tree**

In this problem we are given an integer array `nums` that is sorted in ascending order. We are tasked to convert it to a height-balanced tree. 

We are going to be using a divide and conquer approach implemented via recursion to solve this problem. We create a function `buildBST(left, right)` that puts the middle array as the root of the tree. We then recursively call it to create subtrees. We can do this since we know that the array is sorted.

We create our function. If left is greater than right, we are not able to find a valid middle point, so we return `None`. 

```Python
def buildBST(left, right):
    if left > right:
        return None
```

Then we find the midpoint and make it the root of the subtree.

```Python
    mid = left + (right - left)//2
    root = TreeNode(nums[mid])
```

Then we recursively call out `buildBST()` function to determine the left and right child nodes of the root of the subtree we just processed.

```Python
    root.left = buildBST(left, mid - 1)
    root.right = buildBST(mid + 1, right)
```

Once we have processed the entire tree, we return the root. When the recursion stack is empty we are left with height balanced tree that contains each node. 

```Python
    return root
```

We call our function using the entire range of our input array.

```Python
return buildBST(0, len(nums) -1)
```

**Time Complexity**

The time complexity for this solution is <code><i>O(n)</i></code> where `n` is the length of the array. This is because we process each element in the array exactly one time. 

**Space Complexity**

Using this approach, the space complexity is dictated by the size of the recursion stack. Once we find a way to the bottom the recursion stack will have a size equal to the final binary trees height. Since the tree is balanced the height will be `log n`. We get a space complexity of <code><i>O(log n)</i></code>.