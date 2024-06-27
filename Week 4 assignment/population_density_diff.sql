/*Query the difference between the maximum and minimum populations in CITY.

Input Format

The CITY table is described as follows: CITY.jpg*/

SELECT MAX(POPULATION) - MIN(POPULATION) AS population_difference
FROM CITY;
