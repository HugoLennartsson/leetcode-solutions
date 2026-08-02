
## Explanation

**511. Game Play Analysis I**

In this problem we are given a table `Activity`. It contains information about players for a game. We are tasked to write a solution to find the first login date for each player. 

We are going to use a simple approach. We know that we are going to want to select `player_id` and `event_date`. Based on this we can construct our `SELECT` clause. We still need to figure out how to select the smallest `event_date`.

```sql
SELECT player_id, *** as first_login
```

We can find all the information we need from the `Activity` table. We use this to construct our `FROM` clause. 

```sql
FROM Activity
```

Now we just need to group our rows based on `player_id`. If we do this we can use the `MIN()` function to select the smallest value `event_date` in group. The smallest value will be the oldest date, which is what we want.

```sql
GROUP BY player_id 
```

Our final query becomes the following.

```sql
SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id 
```