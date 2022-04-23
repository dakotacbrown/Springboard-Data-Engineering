# SQL query to find all the venues where matches with penalty shootouts were played. 
SELECT 
	sv.venue_name
FROM 
	euro_cup_2016.match_mast as mm
INNER JOIN
	euro_cup_2016.soccer_venue as sv
    ON mm.venue_id = sv.venue_id
WHERE
	mm.decided_by = 'P';