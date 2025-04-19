--
-- @lc app=leetcode id=196 lang=mysql
--
-- [196] Delete Duplicate Emails
--

-- @lc code=start
# Write your MySQL query statement below
WITH DupricateEmail AS (
    SELECT
        MIN(id) AS firstId,
        email
    FROM
        Person
    GROUP BY
        email
    HAVING
        COUNT(*) >= 2
    ORDER BY
        id
)
DELETE FROM
    Person
WHERE
    email IN (SELECT email FROM DupricateEmail) AND id NOT IN (SELECT firstId FROM DupricateEmail);
-- @lc code=end