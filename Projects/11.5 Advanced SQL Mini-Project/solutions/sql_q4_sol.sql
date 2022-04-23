# SQL query to compute a list showing the number of substitutions 
# that happened in various stages of play for the entire tournament
SELECT 
	DISTINCT m.play_stage,
    COUNT(*) OVER(PARTITION BY m.play_stage) AS Num_Of_Subs
FROM 
	euro_cup_2016.player_in_out AS p
    INNER JOIN euro_cup_2016.match_mast AS m
WHERE
	p.match_no = m.match_no AND
	in_out = 'I';