# SQL query to find all the defenders who scored a goal for their teams.
SELECT
	pm.player_name AS Defender_Name
FROM
	euro_cup_2016.goal_details AS gd
    INNER JOIN
		euro_cup_2016.player_mast AS pm
        ON gd.player_id = pm.player_id
WHERE
	pm.posi_to_play = 'DF' OR
    pm.posi_to_play = 'FD';