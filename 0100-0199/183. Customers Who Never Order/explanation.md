
## Explanation

**183. Customers Who Never Order**

In this problem we are given two tables `Customers` and `Orders`. The `Customers` table contains `id` and `name` for each customer. The `Orders` table contains an identification for the order `id` and an identification for the customer `customerId`. We are tasked to find the customers who never order anything.

To get started with this solution, we know that we are going to want select `name`. We find `name` in the `Customers` table. We can construct our `SELECT` clause based on this.

```sql
SELECT name AS Customers 
```

To determine what names are linked together with the customer identifications that do not order, we need to combine the `Customers` and `Orders` tables. We construct our `FROM` clause with this in mind. 

```sql
FROM Customers AS c LEFT JOIN Orders AS o on c.id = o.customerId
```

Now we want to filter our rows. We want the rows in `Customers` that have an `id` that is not equal to any `customerId` in the `Orders` table. Since we use `LEFT JOIN` in our `FROM` clause every row in `Customers` will be featured. For all rows in `Orders` where `customerId` matches `id` in `Customers`, they will join on those columns. However, if there is no matching identifications the temporary columns from `Orders` will be null. These are the columns we are looking for. 

```sql
WHERE o.customerId IS NULL 
```

Our final solution becomes the following.

```sql
SELECT name AS Customers 
FROM Customers AS c LEFT JOIN Orders AS o on c.id = o.customerId
WHERE o.customerId IS NULL 
```