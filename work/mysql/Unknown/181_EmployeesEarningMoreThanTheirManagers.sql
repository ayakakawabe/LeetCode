--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
# Write your MySQL query statement below
SELECT name AS Employee
FROM Employee
WHERE
    salary >= (
        SELECT Manager.salary
        FROM Employee AS Manager
        WHERE Manager.id = Employee.managerId
    )
-- @lc code=end

