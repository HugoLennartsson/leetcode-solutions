
## Explanation

**21. Merge Two Sorted Lists**

In this problem we are given the heads of two sorted linked lists `list1` and `list2`. We are tasked to merge the two lists into one sorted list. We are then to return the head of the merged linked list.

We start by declaring a dummy ListNode. The dummy is going to be used to keep track of the start of the merged list. We are going to add our nodes in order using the dummy as head. 

```Python
dummy = ListNode()
tail = dummy
```

Following, we iterate through the linked lists. For each node pair we are comparing we check which of the two has the smaller value. We add the smaller value to the tail of the dummy and then move one node forward the values corresponding linked list. We also move our tail one step forward, so it is ready to add another value next iteration.

```Python
while list1 and list2:
    if list1.val < list2.val:
        tail.next = list1
        list1 = list1.next
    else:
        tail.next = list2
        list2 = list2.next
    tail = tail.next
```

When we have reached the end of one of the lists we simply add all of the remaining elements in the other list to the end of our tail. We know all of the elements remaining are larger than the once already in our tail, because otherwise they would have been added in the while loop. 

```Python
tail.next = list1 if list1 else list2
```

Since we kept track of the head of our tail using our `dummy` we can simply return the next node after dummy. That node will be the start of our sorted merged list.

```Python
return dummy.next 
```

**Time Complexity**

The maximum amount of iterations of our while loop happens when the second to last element is in one of the lists and the last element is in the other. This forces us to iterate through the entire length of both linked lists. We get a time complexity of `O(n + m)` where `n = len(list1)` and `m = len(list2)`.