-- 20221107
-- Lv2_131529_카테고리별상품개수구하기
-- PRODUCT 테이블에서 상품 카테고리 코드(PRODUCT_CODE 앞 2자리) 별 상품 개수를 출력하는 SQL문을 작성해주세요. 
-- 결과는 상품 카테고리 코드를 기준으로 오름차순 정렬해주세요.

SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY 1
ORDER BY 1