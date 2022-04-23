# SQL query to find the country where the most assistant referees come from, 
# and the count of the assistant referees
SELECT
	sc.country_name,
    sc.country_id,
    SUM(COUNT(ass_ref_id)) OVER (PARTITION BY country_id) AS Most_Refs,
    (SELECT 
		COUNT(*)
    FROM
		euro_cup_2016.asst_referee_mast
    ) AS Total_Asst_Refs
FROM
	euro_cup_2016.asst_referee_mast AS arm
    INNER JOIN
	euro_cup_2016.soccer_country AS sc
    ON arm.country_id = sc.country_id
GROUP BY
	arm.country_id
ORDER BY
	Most_Refs DESC
LIMIT 1;
