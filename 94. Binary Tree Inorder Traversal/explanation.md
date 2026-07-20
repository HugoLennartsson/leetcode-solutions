
## Explanation

**94. Binary Tree Inorder Traversal**

In this problem we are given the `root` of a binary tree. We are tasked to return the inorder traversal of its nodes values. 

To solve this problem we are going to use a stack. 

We start by declaring some auxiliary data structures we are going to be using. 

```Python
result = []
stack = []
curr = root
```

Then we start processing the tree, starting at the root. When our stack is empty and we do not have current node that we are processing, we know that we have processed the entire tree.

```Python
while curr or stack:
```

We use a while loop to go as far left as possible from our current root. As we go left, we add the nodes to our stack. Once we have reached the leaf node our while loop is going to exit. 

```Python
    while curr: 
        stack.append(curr)
        curr = curr.left
```

When we exit the while loop we pop our stack. The element we pop will always be the the leftmost node in the stack. We add that value to our `result` list.

```Python
    curr = stack.pop()
    result.append(curr.val) 
```

After that we set our current node to the right child node of the node we popped. If there is a node there we will go as far left using it as our starting point. If it is none, we will just pop the stack and process that node.

```Python
    curr = curr.right
```

Once we have processed the entire tree we return our `result`.

**Time Complexity**

In this solution we process each node once. This gives us a time complexity of <code><i>O(n)</i></code> where `n` is the number of nodes in the tree.

**Space Complexity**

Our space complexity is going to be determined by the size of our stack throughout runtime. The stack holds the nodes along the current path from the root down to a leaf. This gives our solution a time complexity of <code><i>O(h)</i></code> where `h` is the height of the tree.