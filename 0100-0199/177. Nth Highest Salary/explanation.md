
## Explanation

**177. Nth Highest Salary**

In this problem we are given a table `Employee`. We are then tasked to find the `Nth` highest salary featured in the employee table. If there are less than `n` distinct salaries, we are told to return `null`.

The main part of our strategy is going to involve using `OFFSET`. OFFSET can be used to skip a specific number of rows. This is often used to handle pagination. 

To solve this, we start by creating a general structure for the query. We know that we want to select salary, and also that we are interested in unique salaries. We also know that we want to select the rows from the `Employee` table. Based on this we can get something started.

```sql
SELECT DISTINCT e.salary
FROM Employee AS e
```

At this point we have all distinct salaries, now we need to somehow filter these rows. We can start by ordering them. Since we are looking for the Nth **highest** salary, it might be a good idea to order them descending. This gives us the highest salary at the first row.

```sql
ORDER BY e.salary DESC
```

To get the `Nth` highest salary we are going to be using the `LIMIT` clause combined with the `OFFSET` clause. `LIMIT` is going to dictate how many rows that we return. Since we only want to return one row, the one with the `Nth` highest salary, we set it to `1`. As stated above `OFFSET` tells us how many rows we want to skip. The Nth largest salary is going to be at row `N` so we need to skip N - 1 rows to get there. 

```sql
LIMIT 1 OFFSET N - 1
```

Our final solution is the following.

```sql
SELECT DISTINCT e.salary
FROM Employee AS e
ORDER BY e.salary DESC
LIMIT 1 OFFSET N - 1
```
