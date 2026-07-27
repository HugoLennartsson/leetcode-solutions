
## Explanation

**141. Linked List Cycle**

In this problem we are given the `head` of a linked list. We are tasked to find out if there is a cycle in the linked list. If so we are to return `True`, otherwise `False`. It is also mentioned that we should use constant memory to solve this problem. 

Our solution is going to be based on <a href="https://en.wikipedia.org/wiki/Cycle_detection">Floyd’s Cycle-Finding Algorithm</a>. The idea of the algorithm is that we can make use of the relative speed between two pointers to find out if there is a circle. By moving one pointer two steps for every step of the other pointer, the gap between the two shrinks by one in case of a cycle. This means that the size of the gap will always reach zero if there is a cycle. 

We start by initializing our two pointers to the start of the linked list.

```Python
slow = fast = head
```

Then we start our while loop. If there is not a cycle in the linked list we will reach a point where the next node is None. Naturally the `fast` pointer will reach the end first. At that point we want to end the loop and since we are able to determine that there is no cycle in the linked list. For each iteration of our loop we move our `fast` pointer two step and our `slow` pointer one step. 

```Python
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

If we find that our `fast` and `slow` pointers point at the same node, we know that there is a cycle in the linked list. In that case we return `True`.

```Python
    if slow == fast:
        return True
```

If we exit out of the while loop it means that we found the end of the linked list. That means that there is no cycle, so we return `False`.

```Python
return False 
```

**Time Complexity**

Using this approach there are two scenarios that could occur. Scenario 1 is that there is no cycle. If that is the case our `fast` pointer will reach the end of the linked list in about `n/2` steps where `n` is the number of nodes in the linked list. Scenario 2 is when there is a cycle. In this case we can split the analysis in to two parts. Before entering the cycle the `slow` pointer can takes fewer than `n` steps. Inside of the cycle the maximum distance between the `slow` and the `fast` pointer is at most `n`. Combining these two we can determine that the total number of iterations will be at most `2n`. Both scenarios lets us conclude that this solution has a time complexity of <code><i>O(n)</i></code>. 


**Space Complexity**

In this solution we only rely on two pointers. The number of pointers stay the same no matter the input size. This means that our space complexity if <code><i>O(1)</i></code>.