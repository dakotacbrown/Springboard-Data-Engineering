# SQL query to find referees and the number of matches they worked in each venue.  
SELECT
	mm.referee_id,
    sv.venue_id,
    sv.venue_name,
    COUNT(sv.venue_id) OVER (PARTITION BY mm.referee_id) AS Total_Venues 
FROM
	euro_cup_2016.match_mast AS mm
    INNER JOIN
		euro_cup_2016.soccer_venue AS sv
        ON mm.venue_id = sv.venue_id
ORDER BY
    Total_Venues DESC;