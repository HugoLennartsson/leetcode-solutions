
## Explanation

**596. Classes With at Least 5 Students**

In this problem we are given a table `Courses`. We are tasked to write a solution to find all classes that have at least five students.

Based on the examples we can construct our `SELECT` clause. We know that we want to select `class`.

```sql
SELECT class 
```

We have all information needed in the Courses table to determine how many student the individual courses have. This lets us construct our `FROM` clause.

```sql
FROM COURSES
```

Now we have a bunch of rows with information about a student and a class. We need to group these rows in order to find out how many student takes each course. Since the `student` is the primary key, we can safely assume that students are unique. This means a student only can attend one `class`. We group the rows based on class.

```sql
GROUP BY CLASS
```

Now the rows are grouped. The number of rows in each group represents the number of students taking a `class`. Using the `HAVING` clause combined with the `count()` function we can filter the rows so only the once with five or more rows remain.

```sql
HAVING COUNT(*) >=5
```

Our final query is the following.

```sql
SELECT class 
FROM COURSES
GROUP BY CLASS
HAVING COUNT(*) >=5
```