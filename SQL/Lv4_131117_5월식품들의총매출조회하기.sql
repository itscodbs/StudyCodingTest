-- 20221109
-- Lv4_131117_5월식품들의총매출조회하기
-- FOOD_PRODUCT와 FOOD_ORDER 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성해주세요.
-- 이때 결과는 총매출을 기준으로 내림차순 정렬해주시고 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬해주세요.

SELECT PRODUCT_ID, PRODUCT_NAME, SUM(PRICE * AMOUNT) AS TOTAL_SAELS
FROM FOOD_PRODUCT JOIN FOOD_ORDER
USING (PRODUCT_ID)
WHERE DATE_FORMAT(PRODUCE_DATE, '%Y-%m') = '2022-05'        
GROUP BY 1
ORDER BY 3 DESC, 1