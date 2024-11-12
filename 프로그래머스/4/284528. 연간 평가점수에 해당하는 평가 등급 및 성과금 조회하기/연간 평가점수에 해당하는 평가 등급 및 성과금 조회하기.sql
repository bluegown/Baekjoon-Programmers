-- 코드를 작성해주세요
SELECT E.EMP_NO AS EMP_NO,E.EMP_NAME AS EMP_NAME,
(CASE WHEN AVG(G.SCORE) >= 96 THEN 'S'
WHEN AVG(G.SCORE) >= 90 THEN 'A'
WHEN AVG(G.SCORE) >= 80 THEN 'B'
ELSE 'C' END) AS "GRADE",
(CASE WHEN AVG(G.SCORE) >= 96 THEN 0.2 * E.SAL 
WHEN AVG(G.SCORE) >= 90 THEN 0.15 * E.SAL 
WHEN AVG(G.SCORE) >= 80 THEN 0.1 * E.SAL 
ELSE 0 END) AS "BONUS"
FROM HR_EMPLOYEES E
JOIN HR_GRADE G
ON E.EMP_NO = G.EMP_NO
GROUP BY E.EMP_NO
ORDER BY EMP_NO ASC
