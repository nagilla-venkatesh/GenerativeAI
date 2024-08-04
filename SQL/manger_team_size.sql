-- Write a query to identify the manager with the biggest team size.

SELECT manager_id, COUNT(employee_id) AS team_size
FROM Employees
GROUP BY manager_id
ORDER BY team_size DESC