# SQL query to find the players, their jersey number, and playing club 
# who were the goalkeepers for England in EURO Cup 2016
SELECT
	pm.player_id,
    pm.jersey_no,
    pm.player_name,
    pm.playing_club
FROM 
	euro_cup_2016.player_mast AS pm
    INNER JOIN
		euro_cup_2016.soccer_country AS sc
        ON pm.team_id = sc.country_id
WHERE
    sc.country_id = 1206 AND
    pm.posi_to_play = 'GK';