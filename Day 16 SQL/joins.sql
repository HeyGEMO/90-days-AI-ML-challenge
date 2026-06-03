#types
#inner join -> intersection
#outer joins
#left join ->all left side
#right join -> all right side
#full join-> all data combined

alter table stu
rename to student;

alter table student 
change rollno id int;
select * from student;

create table course(
id int primary key,
course varchar(50)
);
insert into course(id,course) values
(101,'english'),
(102,'math'),
(103,'science'),
(104,'computer');
select * from course;

select * from student
inner join course
on student.id=course.id;

#alias -> alternate name
#for eg. student as s

select * from student
left join course
on student.id=course.id;

select * from course
right join student
on course.id=student.id;

#full join in mysql
select * from student as s
left join course as c
on s.id=c.id
union
select * from student as s
right join course as c
on s.id=c.id;

#left exclusive join -> left only
select * from student as a 
left join course as b
on a.id=b.id
where b.id is null;

#right exclusive join -> right only
select * from student as a
right join course as b
on a.id=b.id
where a.id is null;

#self join
#regural join - join the table with itself
use company;
create table employee(
id int primary key,
name varchar(50),
manager_id int
);
insert into employee(id,name,manager_id) values
(101,'rikesh',103),
(102,'hari',104),
(103,'bibek',null),
(104,'prazwol',103);

select * from employee;

select * 
from employee as a
join employee as b
on a.id=b.manager_id;

select a.name,b.name from employee as a
join employee as b
on a.id=b.manager_id;

select a.name as manager_name ,b.name from employee as a 
join employee as b
on a.id=b.manager_id;

#union -> unique records
select name from employee
union 
select name from employee;

#union all -> allow duplicates
select name from employee
union all
select name from employee;

