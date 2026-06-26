
## Explanation

**181. Employees Earning More Than Their Managers**

In this problem we are tasked to find the employees that earn mor than their managers. We are given the table `Employee` which contains information about id, name, salary and the id of their manager. To do this we need to somehow differentiate between workers and managers. 

We create a cartesian product using the employee table twice. We call one of them workers and one managers. We know that we are going to want to select the workers name from the cartesian product.

```sql
SELECT workers.name AS employee 
FROM Employee AS workers, Employee AS managers
```

Now we need to filter the cartesian product in order to find the employees that meet the requirement. There are two conditions each row has to fulfill in order to be meet the problem requirement. First we check if the workers manager id is the same as the managers personal id. Then we check if the workers salary is greater than the managers salary. 

```sql
WHERE workers.managerId = managers.id AND workers.salary > managers.salary
```

