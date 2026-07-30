
## Explanation

**577. Employee Bonus**

In this problem we are given two tables `Employee` and `Bonus`. We are tasked to write a solution that reports the name and bonus amount of each employee that has a bonus less than `1000` or did not get a bonus.

We can easily construct our SELECT clause since we know we should return `name` and `bonus`.

```sql
SELECT name, bonus
```

To get the information we need to determine if an employee has gotten a bonus less than `1000` or no bonus at all we need to get information from both the `Employee` and `Bonus` table. We know that the employees that did not get a bonus are not in the `Bonus` table. Therefore we need all rows from the `Employee` table. The only rows that interest us in the `Bonus` table are the ones that have matching ids in the `Employee` table. Therefore we decide to use `LEFT JOIN`.

```sql
FROM Employee e LEFT JOIN Bonus b ON e.empId = b. empId
```

Now we just need to filter the rows. This is simple. We check if the bonus is `NULL` or less than `1000`.

```sql
WHERE b.bonus < 1000 OR b.bonus IS NULL
```