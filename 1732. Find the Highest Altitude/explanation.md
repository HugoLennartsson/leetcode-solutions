
## Explanation

**1732. Find the Highest Altitude** 

In this problem we are given a list of net gains in altitude between points on a road trip. We are tasked to return the highest altitude during the road trip. 

We start by initializing two variables. One to keep track of our current altitude through out the road trip, and one to keep track of the largest altitude.

```python
largest_altitude = 0
current_altitude = 0
```

After that we handle the edge case where the list is empty. This is actually not required since the constraints tell us that the list will have at least the length `1`. 

```python
if not gain:
    return 0
```

Then we get to the main loop. We iterate through the list and update our current altitude for each point. If we find that our point has an altitude that is higher than the previously highest altitude, we save it in out `largest_altitude` variable. When we have iterated through the list we return the largest altitude we found. 

```python
for alt_gain in gain:
        current_altitude += alt_gain
        if current_altitude > largest_altitude:
            largest_altitude = current_altitude
return largest_altitude
```

**Time Complexity** 
We iterate through the list once. The list is `n` items long. Therefore the time complexity is <code><i>O(n)</i></code>.