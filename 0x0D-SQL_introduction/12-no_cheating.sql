-- update the score of Bob to 10 in the table second_table
UPDATE `second_table`
SET `score` = "10"
WHERE `name` = "Bob";
SELECT `score`, `name` FROM `second_table` ORDER BY `score` DESC;
