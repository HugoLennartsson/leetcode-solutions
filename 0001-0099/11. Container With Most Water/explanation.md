
## Explanation

**11. Container With Most Water**

In this problem we are given an array `height` of the length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`. We are tasked to find the two lines that together with the x-axis forms the container with the most water. We are to return the maximum amount of water a container can store.

The overall tactic for this problem is going to be using two pointers going from the endpoints of the array inwards. As we do this we keep track of the maximum amount of water a container has been able to hold so far. 

We start by initializing our pointers as well as an integer variable to keep track of the max water encountered so far. 

```Python
left = 0
right = len(height) - 1
max_water = 0 
```

After that we start searching the array. We start from the endpoints of the array, and iteratively move the pointers closer together. For each of the line pairs that we compare, we calculate the area of the water their container is able to hold. We know that the shorter line will dictate the height of the container. The width will be decided by how many indexes apart the lines are in the array. We compare this to the maximum water we have encountered so far. If it is greater we store it as our new `max_water`.

```Python
while left < right:
    curr_height = min(height[left], height[right])
    curr_width = right - left
    curr_area = curr_height * curr_width

    max_water = max(max_water, curr_area)
```

When that is done, we move the pointer that is pointing at the shorter line one step towards the other line. We do this since the shorter line is the limiting factor. No matter how tall the line after the taller line is, it will be guaranteed to decrease the max volume of water when paired with the shorter line. 

```Python
    if height[left] < height[right]:
        left += 1
    else: 
        right -= 1
```

When our left pointer is at the same index as our right pointer, we have checked all containers that we need to check in order to determine the maximum water. We return it.

```Python
return max_water
```

**Time Complexity**

In each iteration either the `left` pointer moves to the right or the `right` pointer moves to the left. It will take linear time for the pointers to meet, therefore <code><i>O(n)</i></code>.

**Space Complexity**

We only use scalar variables that do not scale with input size, we get constant space <code><i>O(1)</i></code>.