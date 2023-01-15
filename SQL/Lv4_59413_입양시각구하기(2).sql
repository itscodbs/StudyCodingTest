-- Lv4_59413_입양시각구하기(2)
-- 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 
-- 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 
-- 이때 결과는 시간대 순으로 정렬해야 합니다.

SET @hour := -1;

SELECT (@hour := @hour + 1) AS HOUR,
        (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23;        

-- 문제풀이
-- 여기서 말한 SET 은 SQL에서 ‘변수 할당'의 역할이라고 말할 수 있으며 변수 이름은 꼭 @변수명 형태로 선언해야 한다. 
-- 또한, SET 이외에 = 는 SQL에서 비교 연산자라고 생각하기 때문에 변수 선언 및 값 대입 같은 경우 :=를 사용한다. 

-- SET @hour := -1; 은 0부터 시작시키기 위해 -1로 초기화. (1부터 시작하므로)

-- (@hour := @hour + 1)은 1씩 증가값 주기

-- (SELECT COUNT(*) 
-- FROM ANIMAL_OUTS 
-- WHERE HOUR(DATETIME) = @hour) 
-- 같은 경우, 테이블 ANIMAL_OUTS에 있는 HOUR(DATETIME)의 개수를 반복적으로 파악해 @hour에 넣겠다는 의미이다.