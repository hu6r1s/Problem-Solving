SELECT DATE_FORMAT(N.SALES_DATE, "%Y-%m-%d") SALES_DATE, N.PRODUCT_ID, N.USER_ID, N.SALES_AMOUNT
FROM ONLINE_SALE N
LEFT JOIN OFFLINE_SALE F
ON N.PRODUCT_ID=F.PRODUCT_ID
WHERE N.SALES_DATE LIKE "2022-03-%"
UNION
SELECT DATE_FORMAT(F.SALES_DATE, "%Y-%m-%d") SALES_DATE, F.PRODUCT_ID, NULL USER_ID, F.SALES_AMOUNT
FROM ONLINE_SALE N
RIGHT JOIN OFFLINE_SALE F
ON N.PRODUCT_ID=F.PRODUCT_ID
WHERE F.SALES_DATE LIKE "2022-03-%"
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;

# SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
# FROM ONLINE_SALE
# WHERE SALES_DATE LIKE "2022-03-%"
# UNION 
# SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") SALES_DATE, PRODUCT_ID, NULL USER_ID, SALES_AMOUNT
# FROM OFFLINE_SALE
# WHERE SALES_DATE LIKE "2022-03-%"
# ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;