SELECT HOUR(DATETIME) HOUR, COUNT(ANIMAL_ID) COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 20 
GROUP BY HOUR
ORDER BY HOUR;