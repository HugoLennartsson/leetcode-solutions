
## Explanation

**100. Same Tree**

In this problem we are given the roots of two binary trees `p` and `q`. We are tasked to write a function that checks if they are the same or not. 

We are going to use recursion to solve this problem. 

For each of the nodes there are three cases we check. If both `p` and `q` are equal to None, we know that we have reached a leaf node. If only one of `p` and `q` is equal to None we know that the trees cannot be the same. Additionally, if the node we are processing in `p` and `q` contains different values the trees are different.

```Python
if not p and not q:
    return True
if not p or not q: 
    return False
if p.val != q.val:
    return False
```

If none of these conditions are met we know that the current processed nodes are equal. When that is the case, we check the left and right children of the processed nodes. We repeat this until we find out that the trees differ or until we have processed the entire tree. 

```Python
return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

**Time Complexity**

Using the above strategy we traverse both trees simultaneously. As soon as there is a mismatch it stops. The smaller tree dictates the number of recursion calls. This gives us a time complexity of <code><i>O(min(n,m))</i></code> where `n` and `m` are the number of nodes in `p` and `q`.

**Space Complexity**

Our space complexity is determined by the maximum dept of the recursion stack. This means that on average our space complexity will be the minimum height between the two trees, <code><i>O(min(H<sub>p</sub>, H<sub>q</sub>))</i></code>. 