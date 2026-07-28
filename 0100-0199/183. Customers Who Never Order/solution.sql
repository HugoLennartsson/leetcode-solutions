-- Write your PostgreSQL query statement below
SELECT name AS Customers 
FROM Customers AS c LEFT JOIN Orders AS o on c.id = o.customerId
WHERE o.customerId IS NULL 