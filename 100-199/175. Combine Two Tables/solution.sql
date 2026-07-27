-- Write your PostgreSQL query statement below
SELECT firstname, lastName, city, state
FROM Person AS p LEFT JOIN Address as a ON p.personId = a.personId 