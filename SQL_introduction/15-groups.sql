-- lists score and number of records per score, sorted by number of records (descending)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
