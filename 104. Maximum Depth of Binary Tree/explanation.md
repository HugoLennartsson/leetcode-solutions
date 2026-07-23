
## Explanation

**104. Maximum Depth of Binary Tree**

In this problem we are given the `root` of a binary tree. We are tasked to find and return the maximum depth of the tree. 

Our strategy for this problem is going to be using depth first search. We use a stack to do this. On the stack we put tuples with the node and an integer value representing the nodes height. 

We start by covering the edge case where we are the number of nodes in the tree is 0. If that is the case the tree has a height of 0. 

```Python
if not root:
    return 0
```

Then we initialize our `stack`. As stated above, we store `node-height` tuples in the stack. We also create an integer variable `max_depth` for keeping track of the maximum depth we have encountered so far.

```Python
stack = [(root, 1)]
max_depth = 0
```

Now we can start processing the tree. For each node in the tree we compare its depth to the `max_depth`. If its depth is larger we store it in `max_depth`. Then we check if our current node has any child nodes. If it has any, we add them to the stack. We repeat this until the stack is completely empty, meaning we have processed all nodes in the tree. 

```Python
while stack:
    node, depth = stack.pop()
    max_depth = max(max_depth, depth)
    if node.left: stack.append((node.left, depth + 1))
    if node.right: stack.append((node.right, depth + 1))
```

Once we have processed the entire tree, we return `max_depth`.

```Python
return max_depth
```

**Time Complexity**

In this solution we need to process each node in the tree once. This gives us a time complexity of <code><i>O(n)</i></code> where `n` is the number of nodes in the tree.

**Space Complexity**

The space complexity of this solution is dictated by the size of our stack during runtime. The stack will be the largest when it reaches the lowest level in the tree. The path will have the length of the height of the tree. This gives us a space complexity of <code><i>O(h)</i></code> where h is the height of the tree.