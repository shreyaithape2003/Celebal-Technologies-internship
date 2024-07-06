-- Create a new table with selected columns in the destination database
CREATE TABLE destination_table AS
SELECT column1, column2, column3
FROM source_table;

-- Insert data into the new table
INSERT INTO destination_table (column1, column2, column3)
SELECT column1, column2, column3
FROM source_table;
