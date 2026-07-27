
## Explanation

**595. Big Countries** 

In this problem we are tasked to find all countries considered big. In the problem description it is described that big countries are those who have at least an area of at least three million or a population of at least twenty-five million. To solve this problem we query the `World` table by selecting the columns `name`, `population` and `area`. To filter this we use a `WHERE` clause. In the predicate we use OR to cover both the cases mentioned in the problem description.

```sql
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000
```