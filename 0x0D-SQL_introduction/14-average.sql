-- computes the score average of all records in the table second_table
INSERT INTO second_table (SELECT AVG(score) FROM second_table)
AS second_table
