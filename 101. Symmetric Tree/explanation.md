
## Explanation

**101. Symmetric Tree**

In this problem we are given a `root` of a binary tree. We are to check if the tree is symmetric around its center.

We are going to be using a recursive approach for this solution. The main idea is that we split the tree down the middle and recursively check if the left subtree match the right subtree reflected. 

There are three things we need to keep track of in order to determine if a node from the left subtree matches a node from the right subtree. If one of the nodes are `None`, that means that the other also has to be `None` for the tree to be symmetrical. If it is not, we can safely determine that the tree is not symmetrical. We also know that the values of the two nodes must match. We use these three conditions to process each mirrored node pair. 

```Python
def isMirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (left.val == right.val and
            isMirror(left.left, right.right) and 
            isMirror(left.right, right.left))
```

Now we simply call our `isMirror()` function using the `left` and `right` child nodes of our root. 

```Python
return isMirror(root.left, root.right)
```

**Time Complexity**

In the worst case scenario we need to visit every node to confirm that the tree is symmetrical. This gives us a time complexity of <code><i>O(n)</i></code> where `n` is the number of nodes in the tree. 

**Space Complexity**

The space complexity is dictated by the size of the recursive call stack. We will recursively call our way to the bottom of the tree. This means that the height of the tree `h`, determines our space complexity. The space complexity of our solution is therefore <code><i>O(h)</i></code>.