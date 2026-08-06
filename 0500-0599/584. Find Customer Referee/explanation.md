
## Explanation

**584. Find Customer Referee**

In this problem we are given a table `Customer`. We are tasked to find the names of the customers that are either referred by any customer with a different id than 2 or not referred by any other customer.

We are looking for the `name` of the customers that we can find in the `Customer` table. This information allows us to construct our `SELECT` and `FROM` clauses.

```sql
SELECT name 
FROM Customer
```

Now we need to filter our rows. We can construct our `WHERE` clause based on the two conditions given in the problem description. We check if the `referee_id` is `NULL` or if the `referee_id` is different from 2.

```sql
WHERE referee_id IS NULL OR referee_id <> 2 
```

Our final query is the following.

```sql
SELECT name 
FROM Customer
WHERE referee_id IS NULL OR referee_id <> 2 
```