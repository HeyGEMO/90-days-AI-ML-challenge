create database everest;
use everest;
create table student(rollno int primary key,
name varchar(50),
address varchar(20),
marks float,
grade varchar(5));

insert into student (rollno,name,address,marks,grade) values
(101,'hari narayan chaudhary','butwal',87.2,'A-'),
(102,'Bibek poudel','beni',85.3,'A-'),
(103,'Prazwol bista','ktm',88.5,'A-'),
(104,'Rikesh lama','ktm',92.8,'A'),
(105,'Dipin pokherel','ktm',95,'A'),
(106,'Prajwal dangol','ktm',82.1,'A-'),
(107,'laxman shrestha','ktm',78,'B+');
drop table student;
select * from student;
select address, count(rollno) from student group by address;
select address, avg(marks) from student group by address;
select address, avg(marks) from student group by address order by avg(marks);
select grade from student group by grade order by grade;

#having clause - used for groups 
SELECT 
    address, COUNT(rollno)
FROM
    student
GROUP BY address;
SELECT 
    address, COUNT(rollno)
FROM
    student
GROUP BY address having max(marks)>90;

#general order
select
from
where
group by
having
order by    ASC;

select address 
from student 
where grade='A' 
group by address 
having max(marks)>=90 
order by address asc;
