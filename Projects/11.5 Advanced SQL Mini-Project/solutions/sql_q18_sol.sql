# SQL query to find the highest number of bookings given in one match. 
SELECT
	match_no,
    SUM(COUNT(match_no)) OVER (PARTITION BY match_no) AS Most_Bookings
FROM
	euro_cup_2016.player_booked
GROUP BY
	match_no
ORDER BY
	Most_Bookings DESC
LIMIT 1;