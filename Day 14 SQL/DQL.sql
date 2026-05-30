create database school;
use school;

create table student(
	rollno int primary key,
    name varchar(50)
    );

insert into student( rollno,name) values(101,'ashika'),
(102,'akash'),
(103,'rahul'),
(104,'sandip');

select * from student;

insert into student values(105,'dev');
