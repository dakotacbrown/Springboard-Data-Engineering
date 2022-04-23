# SQL query to find referees and the number of bookings they made for the entire tournament. 
# Sort your answer by the number of bookings in descending order. 
SELECT
	mm.referee_id,
	COUNT(pb.match_no) AS Num_Of_Bookings
FROM
	euro_cup_2016.match_mast AS mm
    INNER JOIN
		euro_cup_2016.player_booked AS pb
        ON mm.match_no = pb.match_no
GROUP BY 
	mm.referee_id
ORDER BY 
	Num_Of_Bookings DESC;