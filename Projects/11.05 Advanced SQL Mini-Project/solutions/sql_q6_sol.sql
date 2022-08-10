# SQL query to find the number of matches that were won by a single point,
# but do not include matches decided by penalty shootout
WITH find_ID AS (
SELECT
	*,
	ROW_NUMBER() OVER (ORDER BY match_no) AS id
FROM 
	euro_cup_2016.match_details),
even AS (
SELECT
    *
FROM
	find_id
WHERE
	id % 2 = 0
),
odd AS (
SELECT
	*
FROM
	find_id
WHERE
	id % 2 != 0
)
SELECT 
	COUNT(*) AS Num_Of_Matches
FROM 
	even AS e
    INNER JOIN
		odd AS o
	ON e.match_no = o.match_no
WHERE
	e.decided_by = 'N' AND
    ABS(e.goal_score - o.goal_score) = 1;