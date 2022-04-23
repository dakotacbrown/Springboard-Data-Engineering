# SQL query to find all available information about the players under contract to
# Liverpool F.C. playing for England in EURO Cup 2016
SELECT
	pm.player_id,
    pm.team_id,
    pm.jersey_no,
    pm.player_name,
    pp.position_id,
    pp.position_desc,
    pm.dt_of_bir,
    pm.age,
    pm.playing_club
FROM 
	euro_cup_2016.player_mast AS pm
    INNER JOIN
		euro_cup_2016.playing_position AS pp
        ON pm.posi_to_play = pp.position_id
WHERE
    playing_club = 'Liverpool';