
## Explanation

**175. Combine Two Tables**

In this problem we are tasked to combine two tables `Person` and `Address` and return a table containing `firstName`, `lastName`, `city` and `state`. If the `personId` is missing then the `Address` table, we should report null. 

To solve this we are going to use a `LEFT JOIN`. A left join will retrieve all records from the left table, and include matching records from the right table. If there is no matching records from the right table NULL values will be included for those columns. This describes exactly what we want. We will use an `ON` clause to determine what column the data base is going to join on. In this case we want to join using the `personId`.

```sql
SELECT firstname, lastName, city, state
FROM Person AS p LEFT JOIN Address as a ON p.personId = a.personId 
```