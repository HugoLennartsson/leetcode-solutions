
## Explanation

**1833. Maximum Ice Cream Bars**

In this problem we are tasked to find the maximum amount of ice cream bars a boy can buy given an array of prices of ice cream bars available and coins the boy has on hand. The problem description also tells us that we need to use counting sort to solve this problem. 

The main idea of this solution is using the frequency array of the sorting algorithm to check how many ice cream bars we can buy. We do not actually need to sort the `costs` array. 

First we need to create an empty frequency array. A frequency array  is an array where each value corresponds to the frequency of its index as a value in another array. For example the array `[2, 0 , 3]` would be the frequency array to the array `[0, 2, 0, 2, 2]`. To create an empty frequency array we need to figure out how many elements it should fit. This can easily be done by checking the max value of the original array. We know that the highest value in the original array will be the highest index we need to take in to account.


```python
max_cost = max(costs)
freq = [0] * (max_cost + 1)
```

We then construct the frequency array by adding `1` to each of the values corresponding index.

```python
for cost in costs:
    freq[cost] += 1
```

Now that we have our frequency array fully constructed it is time to calculate how many ice cream bars the boy can buy. We will keep track of successfully bought ice cream bars using the variable `ans`. We iterate through the frequency array from the cheapest ice creams to the more expensive ones. If the frequency of a cost is `0` we move on to the next cost, there is no ice cream to buy at that price. 

```python
ans = 0

for cost in range(1, max_cost + 1):
    if freq[cost] == 0:
        continue
```

We then check the minimum value of the following, `how many ice cream bars of a certain price is available` and `how many ice cream bars of that price could we afford to buy`. For example if there are `4` ice cream bars that cost of `1` coin each and we have `10` coins, `can_buy` will be `4` because there are `4` ice cream bars available and we can afford `10`. 

```Python
    can_buy = min(freq[cost], coins // cost) 
```

Then we add the amount of ice cream bars the boy successfully bought to `ans`. We also remove the coins that the boy used to buy the ice cream bars. Finally we check if the boy has enough coins left to buy a more expensive ice cream bar. If he does not have enough we break the loop and return the amount of ice cream bars he has bought.

```Python
    ans += can_buy
    coins -= can_buy * cost
    
    if coins < cost:
        break

return ans 
```

**Time Complexity** 

To build the frequency array we need to iterate through the entire `costs` array to find the `max_cost` and to add the values into the empty `freq` array. The final for loop and the construction of the empty `freq` array takes `max_cost` iterations on average. The time complexity will therefore be <code><i>O(n)</i></code> + <code><i>O(n)</i></code> + <code><i>O(max_cost)</i></code> + <code><i>O(max_cost)</i></code> = <code><i>O(n + max_cost)</i></code>. Sorting the array using `.sort()` for example would give us a time complexity of <code><i>O(n log n)</i></code>. This is worse for this problem, because we know that `max_cost` is relatively small. 

**Space Complexity**

The space complexity of this problem is determined by the size of the frequency array. The array scales with the size of the largest integer in the input array. The auxiliary space complexity will therefore be <code><i>O(max_cost)</i></code> where `max_cost` is the maximum value present in the `costs` array.



