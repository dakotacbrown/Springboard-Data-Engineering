# SQL query to find the goalkeeper’s name and jersey number, 
# playing for Germany, who played in Germany’s group stage matches. 
SELECT
	DISTINCT pm.player_name,
    pm.jersey_no
FROM 
	euro_cup_2016.player_mast AS pm
	INNER JOIN 
		euro_cup_2016.soccer_country AS sc
        ON pm.team_id = sc.country_id
        INNER JOIN
			euro_cup_2016.match_details AS md
            ON md.player_gk = pm.player_id
WHERE
    sc.country_id = 1208 AND
    md.play_stage = 'G';