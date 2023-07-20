-- Script list all the cities in califonia
SELECT id , name FROM `cities` WHERE `states_id` = (
	SELECT id FROM states WHERE name = 'Califonia') ORDER BY id ASC;
