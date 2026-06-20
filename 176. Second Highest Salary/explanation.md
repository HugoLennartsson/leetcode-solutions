
## Explanation

**176. Second Highest Salary** 

In this problem we are tasked to find the second highest `distinct` salary in the `Employee` table. We handle this by using an inner query and and outer query. 

Lets start with the inner query. We use `SELECT DISTINCT` to remove any duplicate values for salaries. We want to select them from the `Employee` table. Then we order the unique salaries in descending order. This puts the highest salaries at the top. We then use `LIMIT 1` to tell the database to only return 1 row. We combine this with `OFFSET 1`. This means we skip the first row. 

```sql
SELECT DISTINCT salary 
FROM Employee 
ORDER BY salary DESC
LIMIT 1 OFFSET 1
```

In most cases this will give us the second highest salary. But in edge cases, when there is less than two distinct salaries for example, the query above will return an empty set. To solve this we wrap it inside of a query. 

```sql
SELECT ( ... ) AS SecondHighestSalary
```

This makes it so that the cases where the inner query returns an empty set is interpreted as a null value rather than an empty set. We also call the table `SecondHighestSalary` as requested in the problem description.
