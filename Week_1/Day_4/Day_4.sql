create table students
(
    stu_id int primary key,
    name varchar(50),
    roll_no int,
    age int,
    father_name varchar(50),
    nationality varchar(50)
);


insert into students values(1, "raman", 26, 18,"Amresh", "Indian"),
                            (2, "ram", 2, 19,"Salmon", "French"),
                            (3, "Romeo", 6, 18,"Aman", "Indian"),
                            (4, "Yug", 57, 20,"Sujal", "Indian"),
                            (5, "toshi", 45, 19,"Hemraj", "Indian");
                            
select name from students where roll_no > 20 Order by roll_no DESC;


Select stu_id from students group by nationality ;

update students set age = 20 where name = "raman";

select * from students;

delete from students where age = 20;

select * from students;