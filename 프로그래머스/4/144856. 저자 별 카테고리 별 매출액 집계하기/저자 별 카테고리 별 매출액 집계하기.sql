SELECT B.AUTHOR_ID AS AUTHOR_ID,A.AUTHOR_NAME AS AUTHOR_NAME,B.CATEGORY AS CATEGORY,SUM(S.SALES * B.PRICE) AS TOTAL_SALES
FROM BOOK B
JOIN AUTHOR A
ON B.AUTHOR_ID = A.AUTHOR_ID
JOIN BOOK_SALES S
ON B.BOOK_ID = S.BOOK_ID
WHERE MONTH(S.SALES_DATE) = '01' AND YEAR(S.SALES_DATE) = '2022'
GROUP BY B.AUTHOR_ID,B.CATEGORY
ORDER BY AUTHOR_ID ASC, CATEGORY DESC