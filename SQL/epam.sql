--- on an online recruiting platform, each recruiting company can make a request for their candidates to complete a personalised tasks in three categories: 
--1. SQL, 
--2. algo and 
--3. Bug Fixing. 
--Following the assessment, the company receives a report containing, fro each candidate, their declared years of experience (an integer between 0 and 100) and their score in each category. The score is the number of points from 0 to 100, or Null, which means there was no task in this category. 
--You are given a table, assessments, with the following structure:

--create table assessments (
--id integer not null,
--experience integer not null,
--sql integer,
--algo integer,
--bug_fixing integer, 
--unique(id)
--);

--your task is to write an SQL query that, for each different length of experience, counts the number of candidates with precisely that amount of experience and how many of them got a perfect score in each category in which they were requested to solve tasks (so a Null score is treated as a perfect score). 

--Your query should return a table containing the following columns:
--experience, 
--max (number of assessments achieving the maximum score),
--count (total number of assessments),
--Rows should be ordered by decreasing experience.

SELECT
    experience AS exp,
    SUM(
        CASE
            WHEN (sql = 100 OR sql IS NULL) AND
                 (algo = 100 OR algo IS NULL) AND
                 (bug_fixing = 100 OR bug_fixing IS NULL)
            THEN 1 ELSE 0
        END
    ) AS max,
    COUNT(*) AS count
FROM
    assessments
GROUP BY
    experience
ORDER BY
    experience DESC;
