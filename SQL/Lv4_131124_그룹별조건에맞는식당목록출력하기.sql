-- 20221109
-- Lv4_131124_그룹별조건에맞는식당목록출력하기
-- MEMBER_PROFILE와 REST_REVIEW 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL문을 작성해주세요. 
-- 회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력되도록 작성해주시고, 
-- 결과는 리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬해주세요.


SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS M JOIN REST_REVIEW AS R
USING (MEMBER_ID)
WHERE R.MEMBER_ID IN (SELECT MEMBER_ID
                      FROM REST_REVIEW
                      GROUP BY 1
                      HAVING COUNT(MEMBER_ID) = (SELECT COUNT(MEMBER_ID)
                                                    FROM REST_REVIEW
                                                    GROUP BY MEMBER_ID
                                                    ORDER BY 1 DESC
                                                    LIMIT 1))
ORDER BY 3, 2
