#SQL sub queries -> inner queries -> nested queries
use college;

select avg(marks) from student;

select full_name,marks 
from student 
where marks > (select avg(marks) from student);

select id from student where (id%2)=0;

select full_name,id from student where id%2=0;
#or
select full_name,id from student where id in (select id from student where (id%2)=0);

#using from
select * from student where city='ktm';
select max(marks) from (select * from student where city='ktm') as temp;

#in select
select (select max(marks) from student),full_name from student;

#views
create view view1 as select id,full_name,marks from student;
select * from view1;
select * from view1 where marks>90;
drop view view1;