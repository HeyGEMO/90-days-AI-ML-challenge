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

drop database college;
create database college;
use college;
create table student(
rollno int primary key,
name varchar(50),
marks int not null,
grade varchar(1),
city varchar(20));
insert into student(rollno,name,marks,grade,city) values
(101,'hari',87,'B','butwal'),
(102,'prazwol',90,'A','ktm'),
(103,'rikesh',95,'A','ktm'),
(104,'bibek',85,'B','beni'),
(105,'dipin',92,'A','ktm'),
(106,'prazwol',82,'B','ktm');
select * from student;
select rollno,name from student;
select city from student;
select distinct city from student;
select * from student where marks >80;
select * from student where city='ktm';
select * from student where marks >80 and city ='ktm';
select * from student where marks +10>100;
select * from student where marks between 80 and 85;
select * from student where city in('ktm','butwal');
select * from student where city not in('ktm');
select * from student limit 3;
select * from student where marks>80 limit 3;
select * from student order by marks asc;
select * from student order by marks desc limit 3;
#aggrigate function
select max(marks) from student;
select avg(marks) from student;
select min(marks) from student;
select sum(marks) from student;
select count(name) from student;

