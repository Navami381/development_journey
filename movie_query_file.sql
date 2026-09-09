create database movie_db;
show databases;
use movie_db;

create table movie(
  id int primary key auto_increment,
  title varchar(200) not null,
  year varchar(20) not null,
  run_time int,
  rating decimal(2,1) not null,
  genre enum("action","comedy","thriller","drama","horror") default "action"
);

desc movie;

insert into movie(title,year,run_time,rating,genre) values('abcd',2012,150,8.5,'action');
insert into movie(title,year,run_time,rating,genre) values('kgf',2013,150,9.5,'action');
insert into movie(title,year,run_time,rating,genre) values('cid moosa',2010,150,9.6,'comedy');
insert into movie(title,year,run_time,rating,genre) values('spiderman',2026,120,8.5,'action');
insert into movie(title,year,run_time,rating,genre) values('anabella',2017,140,7.7,'horror');

select * from movie;

select * from movie
 where id=2;
 
 update movie set title="sipderman-brand new day",run_time=150  where id=4;
 select * from movie where id=4;
 
 




