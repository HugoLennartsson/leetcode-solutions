
## Explanation

**197. Rising Temperature**

In this problem we are given a table `Weather`. We are tasked to find all dates with higher temperatures compared to its previous dates. 

To start, we know that we want to return `id`. This is enough information to create our `SELECT` clause.

```sql
SELECT id 
```

Then we somehow need to be able to compare the temperatures from one day with its previous day. We create a sub query for this. We want the `id` from our current day, the current date, the `temperature`. To get the information for the previous day, we use the `LAG()` function. It lets us look backwards at a previous row without having to do a complex self join. The defaults for the `LAG()` function is an offset of one, and if there is no previous row, it defaults to null. 

```sql
FROM (
    SELECT id, 
    recordDate,
    temperature,
    LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
    LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
) t
```

Now that we have the information needed we need to filter it using our `WHERE` clause. We check if our current temperature is larger than the previous one. We combine this with checking if our date is one step ahead of our previous date. This is done using the `INTERVAL`. `INTERVAl` is used to represent a span of time using readable text.

```sql
WHERE temperature > prev_temp
AND recordDate = prev_date + INTERVAL '1 day';
```

Our final solution becomes the following.

```sql
SELECT id 
FROM (
    SELECT id, 
    recordDate,
    temperature,
    LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
    LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
) t
WHERE temperature > prev_temp
AND recordDate = prev_date + INTERVAL '1 day';
```