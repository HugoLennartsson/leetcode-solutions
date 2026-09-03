
## Explanation

**206. Reverse Linked List**

In this problem we are given the `head` of a linked list. We are tasked to reverse the linked list and then return it.

We start by initializing two variables `prev` and `curr`. 

```Python
prev = None
curr = head
```

After that we start our main loop. We iterate though the linked list until we reach the end. We create a variable `nxt` to store the next node after `curr`. We then re-point curr to point at the previous node `prev`. After that we move `prev` and `curr` one step forward. 

```Python
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
```

When we have processed the entire list we return `prev` which will be the last node in the non reversed list.

```Python
return prev
```

**Time Complexity**

We have to iterate through the list exactly one time. This gives us a time complexity of <code><i>O(n)</i></code> where `n` is the length of the linked list.

**Space Complexity**

We use the same number of auxiliary variables regardless of the input size. This gives us constant space complexity <code><i>O(1)</i></code>.