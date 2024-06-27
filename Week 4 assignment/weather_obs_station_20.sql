/*A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.

Input Format

The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude.*/

WITH OrderedLatitudes AS (
    SELECT LAT_N, 
        ROW_NUMBER() OVER (ORDER BY LAT_N) AS RowAsc,
        ROW_NUMBER() OVER (ORDER BY LAT_N DESC) AS RowDesc,
        COUNT(*) OVER () AS TotalCount
    FROM STATION
),
MedianCalculation AS (
    SELECT LAT_N
    FROM OrderedLatitudes
    WHERE RowAsc = (TotalCount + 1) / 2
    OR RowAsc = (TotalCount + 2) / 2
)
SELECT ROUND(AVG(LAT_N), 4) AS median_latitude
FROM MedianCalculation;
