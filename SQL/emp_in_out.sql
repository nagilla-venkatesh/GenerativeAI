https://miro.medium.com/v2/resize:fit:466/format:webp/1*4Ghh47dUY1q2-m3ydip6BA.png

-- In a hospital employees can go inside and outside multiple time.
-- Now we have find the the employees who are inside the hospital.

WITH x as(
SELECT *,ROW_NUMBER() OVER(PARTITION BY emp_id ORDER BY time DESC) AS rnk
FROM hospital)

SELECT * FROM x WHERE rnk=1 AND action='in';
