
## Explanation

**586. Customer Placing the Largest Number of Orders**

In this problem we are given a table `Orders`. We are tasked to write a solution to find the `customer_number` for the customer who have placed more orders than any other customer.

Since we are tasked to find the `customer_number` we know how to construct our `SELECT` clause.

```sql
SELECT customer_number
```

We have enough information to determine the customer with the largest number of orders in the `Orders` table. This lets us determine our `FROM` clause.

```sql
FROM Orders
```

Now we need to group our rows by `customer_number`. To do this we use a `GROUP BY` clause. This will allow us to sort the groups by number of orders. This is done using the `ORDER BY` clause in combination with the `COUNT()` function. When we have done that, we can simply take the first row and return it since we put the group with the largest number of orders at the start. We do this by using the `LIMIT` clause.

```sql
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1
```

The final query becomes the following.

```sql
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1
```