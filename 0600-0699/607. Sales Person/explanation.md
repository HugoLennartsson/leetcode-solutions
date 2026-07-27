
## Explanation

**607. Sales Person** 

In this problem we are given the tables `SalesPerson`, `Company` and `Orders`. The schemas for the tables are found in `problem_description.md`. We are then tasked to find and return the names of all the salespersons who did not have any order related to the company with the name `RED`. 

Our strategy to solve this problem is going to be finding the salespersons who have orders related to company `RED` and then negate the results to find the ones that do not. 

We want something like the following. 

```sql 
SELECT s.name
FROM SalesPerson s
WHERE NOT EXISTS (...) 
```

Now we need to construct the subquery for the `WHERE NOT EXISTS` clause. We can use `SELECT 1` as a dummy placeholder, since the database does not care what data the subquery returns. It only focuses on whether any rows match the condition. 

```sql
WHERE NOT EXISTS (
    SELECT 1
```

In order to have adequate information to determine if a salesperson has handled an order with a certain company we will need to join the `Company` table with the `Orders` table. We will want to `JOIN` the rows where com_id matches in both tables. 

``` sql
    FROM Orders o JOIN Company c ON o.com_id = c.com_id
```

Inside our `WHERE` clause we will check if the company name is `RED` and if the `sales_id` from both the tables matches on the same row. If both of these conditions are filled, we know that the person with that `sales_id` has handled an order with the company `RED`.

```sql 
    WHERE c.name = 'RED' AND o.sales_id = s.sales_id
)
```

Our final query will be the following.

```sql 
SELECT s.name
FROM SalesPerson s
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED' AND o.sales_id = s.sales_id
)
```

We select the names of the people from the `SalesPerson` table that have not processed an order for the company `RED`.

