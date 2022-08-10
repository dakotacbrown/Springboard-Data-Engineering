# SQL query to find the number of matches that were won by penalty shootout
SELECT 
	COUNT(*) AS Penalty_Matches_Won
FROM 
	euro_cup_2016.match_details
WHERE
	decided_by = 'P';