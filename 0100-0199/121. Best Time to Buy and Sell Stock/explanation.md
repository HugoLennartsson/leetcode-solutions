
## Explanation

**121. Best Time to Buy and Sell Stock**

In this problem we are given an array `prices` that represent the price of a stock on different days. We are tasked to find the maximum profit that can be made trading the stock. 

We start by declaring two variables to keep track of the max price and max profit we encounter when iterating through `prices`.

```Python
min_price = float("inf")
max_profit = 0
```

After that we start iterating through the array. There are two things we want to check when doing so. Firstly we want to check if the current stock price we are looking at is smaller than our current `min_price`. If that is the case we set `min_price` to our current stock price. 

```Python
for price in prices:
    if price < min_price:
        min_price = price
```

When we encounter a price that is not smaller than `min_price` we check if the difference between our price and the minimum price encountered is larger than the maximum profit we have calculated so far. If it is we update our `max_profit` by storing that value.

```Python
    elif price - min_price > max_profit:
        max_profit = price - min_price
```

When we have processed the entire array we return the `max_profit`.

```Python
return max_profit
```

**Time Complexity**

In this solution we iterate through the prices array one time. This gives us a linear time complexity <code><i>O(n)</i></code>.

**Space Complexity**

We only make use of two auxiliary variables, giving us constant time complexity <code><i>O(1)</i></code>.