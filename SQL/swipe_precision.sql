-- There are two tables. One table is called swipes that holds a row for every Tinder swipe and contains a boolean column that determines if the swipe was a right or left swipe called is_right_swipe. The second is a table named variants that determines which user has which variant of an AB test.

-- Write a SQL query to output the average number of right swipes for two different variants of a feed ranking algorithm by comparing users that have swiped 10, 50, and 100 swipes in a feed_change experiment.

-- Output the following columns:
-- variant, mean_right_swipes, swipe_threshold, num_users

WITH swipe_ranks AS (
    SELECT 
        swipes.user_id
        , variant
        , RANK() OVER (
            PARTITION BY user_id ORDER BY created_at ASC
        ) AS ranks
        , is_right_swipe
    FROM swipes
    INNER JOIN variants 
        ON swipes.user_id = variants.user_id
    WHERE experiment = 'feed_change'
)

SELECT 
    variant
    , CAST(SUM(is_right_swipe) AS DECIMAL)/COUNT(DISTINCT sr.user_id) AS mean_right_swipes
    , 10 AS swipe_threshold
    , COUNT(DISTINCT sr.user_id) AS num_users
FROM swipe_ranks AS sr
INNER JOIN (
    SELECT user_id
    FROM swipe_ranks
    WHERE ranks >= 10
    GROUP BY 1
) AS subset 
    ON subset.user_id = sr.user_id
WHERE ranks <= 10
GROUP BY 1

UNION ALL

SELECT 
    variant
    , CAST(SUM(is_right_swipe) AS DECIMAL)/COUNT(DISTINCT sr.user_id) AS mean_right_swipes
    , 50 AS swipe_threshold
    , COUNT(DISTINCT sr.user_id) AS num_users
FROM swipe_ranks AS sr
INNER JOIN (
    SELECT user_id
    FROM swipe_ranks
    WHERE ranks >= 50
    GROUP BY 1
) AS subset 
    ON subset.user_id = sr.user_id
WHERE ranks <= 50
GROUP BY 1

UNION ALL

SELECT 
    variant
    , CAST(SUM(is_right_swipe) AS DECIMAL)/COUNT(DISTINCT sr.user_id) AS mean_right_swipes
    , 100 AS swipe_threshold
    , COUNT(DISTINCT sr.user_id) AS num_users
FROM swipe_ranks AS sr
INNER JOIN (
    SELECT user_id
    FROM swipe_ranks
    WHERE ranks >= 100
    GROUP BY 1
) AS subset 
    ON subset.user_id = sr.user_id
WHERE ranks <= 100
GROUP BY 1
