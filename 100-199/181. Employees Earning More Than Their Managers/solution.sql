-- Write your PostgreSQL query statement below
SELECT workers.name AS employee 
FROM Employee AS workers, Employee AS managers
WHERE workers.managerId = managers.id AND workers.salary > managers.salary
