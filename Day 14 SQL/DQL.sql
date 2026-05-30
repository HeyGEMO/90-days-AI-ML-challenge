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

create database xyz;
use xyz;
create table employee (
	id int primary key,
    name varchar(50),
    salary int);
insert into employee(id,name,salary) 
values
(1,"adam",25000),
(2,"bob",30000),
(3,"casey",40000);
select * from employee;