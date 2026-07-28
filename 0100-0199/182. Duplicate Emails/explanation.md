
## Explanation

**182. Duplicate Emails**

In this problem we are given a table `Person` where each row contains information about a persons `id` and `email`. We are tasked to write a solution that reports all duplicate emails. We are also told that it is guaranteed that the email field is not `NULL`.

Lets walkthrough the process of solving this problem. We know that we are looking for emails from the Persons table. This lets gives us the following start.

```sql
SELECT email as Email 
FROM Person
```

Now we have all emails, but we need to find the ones that are duplicates. To do this, we first group our rows by email. We then use `HAVING` combined with `COUNT()` in order to filter these groups. 

```sql
GROUP BY email 
HAVING COUNT(*) > 1
```

Our final solution is the following.

```sql
SELECT email as Email 
FROM Person
GROUP BY email 
HAVING COUNT(*) > 1
```