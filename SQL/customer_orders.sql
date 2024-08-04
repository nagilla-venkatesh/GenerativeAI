-- Write a query to identify customers who placed more than three transactions each in both 2019 and 2020.

SELECT u.name AS customer_name FROM users u 
WHERE u.id IN 
(
    SELECT user_id FROM transactions
    WHERE YEAR(created_at) = 2019
    GROUP BY user_id 
    HAVING COUNT(user_id) >= 3
)
    AND u.id IN (
    SELECT user_id FROM transactions
    WHERE YEAR(created_at) = 2020
    GROUP BY user_id 
    HAVING COUNT(user_id) >= 3
)

