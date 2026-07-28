
## Explanation

**196. Delete Duplicate Emails**

In this problem we are given a table `Person` that contains identification and email on each row. We are tasked to write a solution that deletes all duplicate emails, keeping only the ones with the smallest `id`. 

We can establish our DELETE clause. We know that we want to delete rows from the `Person` table. We also create an alias P1 for this table. 

```sql
DELETE FROM Person p1
```

We use the `USING` clause to join the table we are deleting from to another table. In this case we are joining it to the same table.  

```sql
USING Person p2
```

Now we need to filter these rows. There are two conditions we are looking for. The first one that we want to delete the row with the smallest id, and the second one is that the emails of those ids have to match.

```sql
WHERE p1.id > p2.id
AND p1.email = p2.email
```

The full solution is the following.

```sql
DELETE FROM Person p1
USING Person p2
WHERE p1.id > p2.id
AND p1.email = p2.email
```
