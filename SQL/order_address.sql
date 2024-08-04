--Given a table of transactions and a table of users, write a query to determine if users tend to order more to their primary address versus other addresses.

--Note: Return the percentage of transactions ordered to their home address as home_address_percent.

SELECT 
    ROUND(
        100.0 * SUM(
            CASE
                WHEN t.address_id = u.home_address_id THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS home_address_percent
FROM transactions t
JOIN users u
ON t.user_id = u.id

SELECT 
ROUND( 
SUM(CASE WHEN u.address = t.shipping_address THEN 1 END)
/ COUNT(t.id)
,2)  as home_address_percent
FROM transactions t 
JOIN users u
on t.user_id = u.id