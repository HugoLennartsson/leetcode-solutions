
## Explanation

**83. Remove Duplicates from Sorted List**

In this problem we are given the `head` of a sorted linked list. We are tasked to delete all duplicate elements in the linked list and return it. 

To solve this we are going to traverse through the linked list and look ahead. Based on what we see we will make adjustments.

First off, we check if that our `head` is not None.

```Python
if not head:
    return None 
```

We initialize a variable `current` to keep track of what node we are processing. We start processing the `head` node.

```Python
current = head
```

After that we process the linked list. We need to be able to check our `current` node and the next node. 

```Python
while current and current.next: 
```

We check if our the value of our `current` node is equal to the value of our next node. If it is we move our next pointer to the node after our next node. This makes it so the duplicate node is excluded from the linked list.

```Python
    if current.val == current.next.val:
        current.next = current.next.next
```

If they are not equal, we simply move on to processing the next node.

```Python
    else:
        current = current.next
```

Then we return the head of the new linked list.

```Python
return head
```

**Time Complexity**

Using this solution we need to pass through the linked list one time. This gives us a time complexity of <code><i>O(n)</i></code> where `n` is the length of the linked list.

**Space Complexity**

When using this approach we only rely on two variables that hold our focused node and the next node after. When we run into duplicates we only need to rearrange the node pointers. This means that we use constant space. Our space complexity is <code><i>O(1)</i></code>.