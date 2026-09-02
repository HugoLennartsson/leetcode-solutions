
# Explanation

**203. Remove Linked List Elements**

In this problem we are given the `head` of a linked list. We are tasked to remove all nodes that have a value equal to `val`.

We start by creating a dummy node. We use this to create two auxiliary variables `tail` and `curr`. 

```Python
dummy = ListNode(next=head)
tail, curr = dummy, head
```

When we have that set up we can start with our main loop. We iterate through the linked list until we reach the end, when `curr == None`. We check if our current nodes value matches `val`. If it does we move our tails pointer past the current node. This will exclude it from the linked list. If our current nodes value does not match `val` we simply move our tail forward one step. In either case we move our current node one step forward to process the next node.

```Python
while curr: 
    if curr.val == val:
        tail.next = curr.next
    else:
        tail = curr
    curr = curr.next
```

When we have processed the entire array, we need to return the head of the potentially updated linked list. Our dummy node keeps track of our head, so we can use that.

```Python
return dummy.next
```

**Time Complexity**

We pass through the list once. The solution therefore has a time complexity of <code><i>O(n)</i></code>.

**Space Complexity**

We only use auxiliary ListNode variables, this gives us constant space complexity <code><i>O(1)</i></code>.