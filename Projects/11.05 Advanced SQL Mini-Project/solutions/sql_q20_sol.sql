# SQL query to find the substitute players who came into the field in the first half of play, 
# within a normal play schedule. 
SELECT
    pm.player_id,
    pm.player_name
FROM
	euro_cup_2016.player_mast AS pm
    INNER JOIN
		euro_cup_2016.player_in_out AS pio
        ON pm.player_id = pio.player_id
WHERE
	play_schedule = 'NT'
    AND play_half = 1
    AND in_out = 'I';