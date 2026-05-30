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

create table temp1(
id int,
name varchar(50),
age int,
primary key (id,name));

create table emp(
id int,
salary int default 25000);
insert into emp(id) values (1);
select * from emp;