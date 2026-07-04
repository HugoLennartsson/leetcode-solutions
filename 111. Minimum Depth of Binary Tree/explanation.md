
## Explanation

**111. Minimum Depth of Binary Tree**

In this problem we are tasked to find the minimum depth of a binary tree. The minimal depth of a binary tree will be the depth of the highest leaf node. We can therefore use **breadth first search (BFS)** to traverse the tree. This is a good idea, since the first leaf node encountered is guaranteed to have the minimum depth of the tree. 

Firstly we make sure that the root node is not `None`. 
```python
if not root:
    return 0 
```
If there is no root node in a binary tree we return `0`.

Then we create a double-ended queue. Inside it we store a tuple of the root TreeNode and the depth of the root. 
```python
q = deque([(root, 1)])
``` 

After that we want to process the tree using breadth first search until we find the first leaf node. 

```python
while q:
    node, depth = q.popleft()
```
We take out the first element from the queue, as a node, depth pair. 

```python
    if not node.left and not node.right:
        return depth
```
If the node does not have any children, it is a leaf node. We return the depth of it. We can be sure that the first leaf node encountered in BFS has the minimum depth. 

```python
    if node.left:
        q.append((node.left, depth + 1))
    if node.right:
        q.append((node.right, depth + 1))
```
In case the node was not a leaf, we add any any potential left/right children to the deque. 

**Time Complexity** 

Each node we process during the search process takes constant time to process. In the worst case scenario we will have to check all of the nodes. This gives us a time complexity of <code><i>0(n)</i></code> where `n` is the amount of nodes in the tree. 

**Space Complexity**

Using this approach for the solution is determined by the maximum number of nodes stored in the deque at any given point. In the worst case scenario the tree will be perfectly balanced. For a balanced tree the bottom level contains about half of the total nodes in the entire tree, `n/2` nodes. The maximum size of our queue scales linearly with the number of nodes. This results in our auxiliary space complexity of <code><i>O(n)</i></code> where `n` is the total number of nodes. 

