-- Write SQL for calculating the average salary of employees in each department.

SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id;

-- Write SQL to find the department with the highest average salary.

SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
ORDER BY avg_salary DESC




