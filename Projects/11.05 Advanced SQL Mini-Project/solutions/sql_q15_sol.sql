# SQL query to find the referees who booked the most number of players. 
SELECT
	mm.referee_id,
	COUNT(DISTINCT pb.player_id) AS Num_Of_Bookings
FROM
	euro_cup_2016.match_mast AS mm
    INNER JOIN
		euro_cup_2016.player_booked AS pb
        ON mm.match_no = pb.match_no
GROUP BY 
	mm.referee_id
ORDER BY 
	Num_Of_Bookings DESC;