create database expense_db;
show databases;
use expense_db;



create table expenses (
    id int primary key auto_increment,
    owner varchar(200) not null,
    amount decimal(10,2) not null,
    date date not null,
    category enum("food", "travel", "shopping", "bills", "education") default "food",
    payment_method enum("cash", "upi", "card", "bank_transfer") default "cash"
);

desc expenses;

insert into expenses(owner,amount,date,category,payment_method) values('nithin',1500.70,'2026-07-01','shopping','cash');
insert into expenses(owner,amount,date,category,payment_method) values('zayn',50000,'2026-04-22','travel','bank_transfer');
insert into expenses(owner,amount,date,category,payment_method) values('milly',7800,'2023-07-01','bills','upi');
insert into expenses(owner,amount,date,category,payment_method) values('sadie',2000,'2022-05-01','food','cash');
insert into expenses(owner,amount,date,category,payment_method) values('zendaya',750000,'2024-02-01','education','upi');

select * from expenses;
select * from expenses where id=3;
update expenses set owner="sam",date="2026-01-01" where id=1;

select * from expenses;





