-- 2021109
-- Lv4_131118_서울에위치한식당목록출력하기
-- REST_INFO와 REST_REVIEW 테이블에서 서울에 위치한 식당들의 
-- 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회하는 SQL문을 작성해주세요. 
-- 이때 리뷰 평균점수는 소수점 세 번째 자리에서 반올림 해주시고 결과는 평균점수를 기준으로 내림차순 정렬해주시고, 
-- 평균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬해주세요.

SELECT REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO AS I JOIN REST_REVIEW AS R
USING (REST_ID)
WHERE ADDRESS LIKE '서울%'
GROUP BY 1
ORDER BY 6 DESC, 4 DESC