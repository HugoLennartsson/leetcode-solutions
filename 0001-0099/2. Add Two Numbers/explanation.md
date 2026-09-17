
## Explanation

**2. Add Two Numbers** 

In this problem we are given two non-empty linked lists representing two non-negative integers. They are given in reverse order. Each node contains a single digit, our task is to add the two numbers and return the sum as a linked list. 

We start by setting up a dummy node that we are going to use to build or linked list we are returning later on. We set that node as our current node that we are focusing on. We also create a variable to keep track of any carries that could happen in case the sum of the values from the two nodes is equal to or greater than $10$.

```Python
dummy = ListNode(0)
current = dummy
carry = 0
```

Now we can start our main loop. We want to keep building our linked list as long as there are nodes that we have not processed and as long as we do not have a carry to deal with. That gives us the following loop.

```Python
while l1 or l2 or carry:
```

We setup our values for the two nodes we are handling. If our node contains a value, we store that value. If not we store the value zero to represent the node.

```Python
    val1 = l1.val if l1 else 0 
    val2 = l2.val if l2 else 0
```

After that we calculate the total sum of the two nodes and the carry. We store this in a variable `total`, we also find out if the new sum creates a carry by using integer division by $10$. 

```Python
    total = val1 + val2 + carry
    carry = total // 10 
```

When we have calculated the sum we add a ListNode following our `current` node. We use the modulo operator by $10$ to find the digit we are adding. This does nothing to our sum in case it is less than $10$. However if our sum is double digit, the modulo operator helps us isolate the least significant digit. We also set this node as our `current` node to prepare for the next iteration.

```Python
    current.next = ListNode(total % 10)
    current = current.next
```

Now we only need to move one step forward in the other linked lists. We do this by setting `l1` and `l2` to their next nodes. If there is no next node we simply set it to `None`.

```Python
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
```

Once we have iterated both of the linked list and handled the carry flag, we have built our linked list. Since our `dummy` node keeps track of the start of the linked list we constructed, we just return the next node after the `dummy`.

```Python
return dummy.next  
```

**Time Complexity**

The time complexity of the problem is decided by the number of iterations of the while loop. That number is in turn dictated by how long the linked lists are. The linked list that is the longest will decide how many iterations is needed. That means that the time complexity of the solution can be written as <code><i>O(max(len(n), len(m)))</i></code> where `n` and `m` is the lengths of `l1` and `l2`.

**Space Complexity**

The space complexity is decided by how long the linked list we are building is. That is decided by the longest of `l1` and `l2`. We get a space complexity of <code><i>O(max(len(n), len(m)))</i></code>.