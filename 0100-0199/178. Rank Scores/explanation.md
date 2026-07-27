
## Explanation

**178. Rank Scores**

In this problem we are given a table `Scores` that contains the columns `id` and `score`. We are tasked to query a table that finds the rank of the scores. The rankings are determined using the following rules. 

1. The scores should be ranked from the highest to the lowest.
2. If there is a tie between two scores, both should have the same ranking.
3. After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.

We are also told the result table should be ordered by `score` in descending order.

To construct our solution, a good strategy might be to try to find the general structure of the query. We can create a skeleton where we feature the parts we know how to do, then we just fill in the gaps. 

```sql
SELECT 
    score,
    ... AS rank
FROM Scores 
ORDER BY score DESC;
```

This structure is pretty trivial to come up with, the challenge will be to figure out what rank should be. In this solution we are going to be using the `DENSE_RANK()` window function. Using this, we do not need to create a dedicated subquery for rank. 

```sql
DENSE_RANK() OVER (ORDER BY score DESC) AS rank
```

Lets break down what the line above actually does. `DENSE_RANK()` is a function specifically designed to handle ranking where there are ties. It never skips a rank. `OVER (...)`  tells us what to treat as a window. In our case we did not include any filtering criteria inside `OVER(...)` so it is going to treat all of our rows as a window. Inside we wrote `ORDER BY score DESC` which means all of our rows inside of the window is ordered by `score` in descending order. When the rows are sorted our `DENSE_RANK()` function gives out the scores. 

Lets now combine this with out skeleton structure.

```sql
SELECT 
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores 
ORDER BY score DESC;
```

