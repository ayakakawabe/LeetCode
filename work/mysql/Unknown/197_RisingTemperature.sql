--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--

-- @lc code=start
# Write your MySQL query statement below
WITH preTemperatureTable AS (
    SELECT
        DATE_ADD(recordDate,INTERVAL 1 DAY) AS recordDate,
        temperature AS preTemperature
    FROM
        Weather
)

SELECT
    id
FROM
    Weather
WHERE
    temperature > (
        SELECT preTemperature
        FROM preTemperatureTable
        WHERE recordDate = Weather.recordDate
    );
-- @lc code=end

