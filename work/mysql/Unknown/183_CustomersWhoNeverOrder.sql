--
-- @lc app=leetcode id=183 lang=mysql
--
-- [183] Customers Who Never Order
--

-- @lc code=start
# Write your MySQL query statement below
SELECT Customers.name AS Customers
FROM Customers
WHERE
    Customers.id NOT IN (
        SELECT Orders.customerId
        FROM Orders
    )
-- @lc code=end

