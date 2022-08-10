# SQL query to find the match number for the game with the
# highest number of penalty shots, and which countries played that match.
SELECT 
	md.match_no,
    sc.country_name,
    MAX(md.penalty_score) OVER (PARTITION BY md.match_no) AS Highest_Num_Penalty
FROM 
	euro_cup_2016.match_details as md
INNER JOIN
	euro_cup_2016.soccer_country as sc
WHERE
	md.team_id = sc.country_id AND
	md.decided_by = 'P'
ORDER BY 
	md.match_no DESC
LIMIT 2;