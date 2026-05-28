create database college;
use college;
create table student(
id int primary key,
name varchar(50),
age int not null
);

insert into student value(1,"akash",27);
insert into student value(2,"rahul",28);
insert into student value(3,"sandeep",25);

select * from student;