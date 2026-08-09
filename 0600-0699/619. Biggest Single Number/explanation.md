
## Explanation

**619. Biggest Single Number**

In this problem we are given a table `MyNumbers`. Our task is to find the largest single number. If there is no single number we are to return NULL.

Our strategy is going to involve using a subquery to find all numbers that are single. We can then use the `MAX()` function to find the largest single number.

We start by constructing our `SELECT` clause. We can create an outline of our query based on what we know so far. As previously stated we want to use the `MAX()` function. It is going to take the largest value from the table we create in our subquery. We also know that our output table is supposed to have a column named `num`.

```sql
SELECT MAX(num) AS num
FROM (
    ***
) AS unique_numbers
```

Now we need to figure out how to construct our subquery. It should be enough to get all numbers and then somehow filter them. We have enough information to do this in the `MyNumbers` table. 


```sql
SELECT num
FROM MyNumbers
```

From here we need to filter the rows so the unique numbers remain. We can do this by grouping our rows based on `num` and then remove all groups that are not the size of 1. 

```sql
GROUP BY NUM
HAVING COUNT(num) = 1
```

Now we just need to put it all together.

```sql
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY NUM
    HAVING COUNT(num) = 1
) AS unique_numbers
```