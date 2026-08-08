-- Write your PostgreSQL query statement below
SELECT class 
FROM COURSES
GROUP BY CLASS
HAVING COUNT(*) >=5