create user 'cos'@'%' identified by 'cos1234';

-- 권한부여
GRANT ALL PRIVILEGES ON *.* TO 'cos'@'%';

-- DB 생성
CREATE DATABASE blog CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

-- DB 사용
use blog;

show databases;
select*from all_users limit 10;
SHOW VARIABLES LIKE 'datadir';