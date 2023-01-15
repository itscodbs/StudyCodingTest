use blog;

select * from user;
insert into user values(1, "2023-01-05", "user@naver.com", "user1234", "USER", "cosuser");
delete from user where id=1 ;
show variables like 'c%';

drop database blog;

create database blog character set utf8 default collate utf8_general_ci;

select * from board;
select * from reply;