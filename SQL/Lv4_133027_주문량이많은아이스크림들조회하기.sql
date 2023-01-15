-- 20221108
-- Lv4_133027_주문량이많은아이스크림들조회하기
-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.

SELECT J.FLAVOR 
FROM FIRST_HALF AS F RIGHT JOIN JULY AS J
ON J.FLAVOR = F.FLAVOR
GROUP BY 1
ORDER BY SUM(J.TOTAL_ORDER) + SUM(F.TOTAL_ORDER) DESC
LIMIT 3