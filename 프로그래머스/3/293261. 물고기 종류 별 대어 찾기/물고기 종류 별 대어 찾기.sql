-- 코드를 작성해주세요
SELECT ID, FISH_NAME, INFO.LENGTH AS LENGTH
FROM FISH_INFO AS INFO
JOIN FISH_NAME_INFO AS NAME
ON NAME.FISH_TYPE = INFO.FISH_TYPE -- 조인으로 일단 테이블 한개로 조져주고
WHERE INFO.LENGTH IN (SELECT MAX(LENGTH) FROM FISH_INFO
                     WHERE FISH_TYPE = NAME.FISH_TYPE
                     GROUP BY FISH_TYPE) -- 이렇게 하면 FISH_TYPE별 맥스 길이가 나오게 된다
                     -- 이렇게 해서 각각 행 한개씩 추출 가능
ORDER BY ID
