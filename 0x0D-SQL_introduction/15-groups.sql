-- Lists the number of records with the same score in the table second_table_0
SELECT score, COUNT(score) as number FROM second_table
GROUP BY score ORDER BY number DESC;