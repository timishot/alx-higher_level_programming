-- script that lists the muber of records in score
SELECT `score`, COUNT(`score`) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
