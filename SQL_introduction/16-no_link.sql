-- lists score and name from second_table, excluding rows without a name, ordered by score (highest first)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
