--Query all columns (attributes) for every row in the CITY table.
--The CITY table is described as follows:
--CITY.jpg

SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population)) AS AvgCityPopulation
FROM CITY
JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
GROUP BY COUNTRY.Continent;
