# SQL query to find the number of matches that were won by a single point,
# but do not include matches decided by penalty shootout
SELECT 
	COUNT(DISTINCT match_no) AS Num_Of_Matches,
    IFNULL(goal_score - LAG(goal_score) OVER w, 0) AS diff
FROM 
	euro_cup_2016.match_details
WHERE
	decided_by = 'N'
WINDOW w AS (ORDER BY match_no);