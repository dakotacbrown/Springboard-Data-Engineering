# SQL query to find the number of captains who were also goalkeepers.
SELECT
    COUNT(*) AS Captain_Goalkeepers
FROM
	euro_cup_2016.player_mast AS pm
    INNER JOIN
		euro_cup_2016.match_captain AS mc
        ON pm.player_id = mc.player_captain
WHERE
	pm.posi_to_play = 'GK';