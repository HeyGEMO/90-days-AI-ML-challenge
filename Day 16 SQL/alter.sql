use college;
create table dept(
id int primary key,
name varchar(50)
);
insert into dept
values
(101,'english'),
(102,'math');
SET SQL_SAFE_UPDATES = 0;
update dept
set name='science and technology'
where name='english';
update dept
set id=111
where id=101;

create table teachers(
id int primary key,
course_name varchar(50),
dept_id int,
foreign key (dept_id) references dept(id)
on update cascade
on delete cascade
); 
drop table courses;
insert into teachers
values
(101,'lassan',101),
(102,'gendu',102);
#cascading->change anything from one table can automatically changed in another table
#on delete cascade
#on update cascade
select * from teachers;
select * from dept;

#alter -> to change the schema ->design (columns,datatype,constraints)
alter table student
add column age int;

alter table student
drop column age;

alter table student
add column age int not null default 19;

alter table student modify age varchar(2);

alter table stu
change name full_name varchar(50);

alter table student 
rename to stu;

delete from stu
where marks <80;

alter table stu
drop column stu_age;

select * from stu;

#drop -> delete the table
#truncate -> delete data from table
truncate table student;

#joins -> combining multiple table

