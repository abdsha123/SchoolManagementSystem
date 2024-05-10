create schema school;
USE school;
CREATE TABLE teacher( 
teacherID SMALLINT NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(40) NOT NULL,
contactNum VARCHAR(15) NOT NULL,
email VARCHAR(40) NOT NULL,
qualification VARCHAR(80) NOT NULL,
PRIMARY KEY (teacherID)
);

CREATE TABLE class( 
classID VARCHAR(3),
ClassTeacher SMALLINT,
PRIMARY KEY (classID),
FOREIGN KEY (ClassTeacher) REFERENCES teacher(teacherID)
);

CREATE TABLE Student( 
rollNum SMALLINT NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
dob DATE NOT NULL,
address VARCHAR(40) NOT NULL,
fatherName VARCHAR(30) NOT NULL,
contactNum VARCHAR(15) NOT NULL,
email VARCHAR(40) NOT NULL,
classID VARCHAR(3) NOT NULL,
PRIMARY KEY(rollNum),
FOREIGN KEY (classID) REFERENCES class(classID)
);

CREATE TABLE room( 
roomNum SMALLINT,
roomDescription VARCHAR(20),
locationBlock VARCHAR(80),
seatingCapacity SMALLINT,
PRIMARY KEY (roomNum)
);

CREATE TABLE subjects(
subjectID SMALLINT,
title VARCHAR(20),
subjectDescription VARCHAR(80),
PRIMARY KEY (subjectID)
);

CREATE TABLE result(
examTitle VARCHAR(10) NOT NULL,
academicYear SMALLINT NOT NULL,
rollNum SMALLINT NOT NULL,
subjectID SMALLINT NOT NULL,
maxMarks SMALLINT NOT NULL,
obtainedMarks SMALLINT NOT NULL,
FOREIGN KEY (rollNum) REFERENCES student(rollNum),
FOREIGN KEY (subjectID) REFERENCES subjects(subjectID)
);

CREATE TABLE meeting(
period SMALLINT,
dayOfWeek VARCHAR(15),
classID VARCHAR(3),
roomNum SMALLINT,
subjectID SMALLINT,
FOREIGN KEY (classID) REFERENCES class(classID),
FOREIGN KEY (roomNum) REFERENCES room(roomNum),
FOREIGN KEY (subjectID) REFERENCES subjects(subjectID),
PRIMARY KEY (classID, dayOfWeek, period)
); 



CREATE TABLE teaches(
classID VARCHAR(3),
subjectID SMALLINT,
teacherID smallint,
FOREIGN KEY (classID) REFERENCES class(classID),
FOREIGN KEY (subjectID) REFERENCES subjects(subjectID),
FOREIGN KEY (teacherID) REFERENCES teacher(teacherID)
);

CREATE TABLE booklibrary (
  ISBN int PRIMARY KEY NOT NULL,
  bookName varchar(250) NOT NULL,
  bookDescription varchar(250) NOT NULL,
  bookAuthor varchar(250) NOT NULL,
  bookPrice varchar(250) DEFAULT NULL,
  returnby date ,
  studentID smallint NOT NULL,
  FOREIGN KEY(studentID)REFERENCES student(rollNum)
  
);

CREATE TABLE locker (
  Lockerid int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  LockerName varchar(250) NOT NULL,
  Studentid smallint NOT NULL,
  FOREIGN KEY(Studentid) REFERENCES student(rollNum)
) ;

CREATE TABLE events (
  eventid int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  eventDescription varchar(250),
  eventFor varchar(10) DEFAULT NULL,
  eventPlace varchar(250),
  eventDate date NOT NULL
) ;

CREATE TABLE mediaitems (
  media_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
 mediaURL varchar(250) NOT NULL,
  mediaTitle varchar(250) NOT NULL,
  mediaDescription varchar(250) ,
  mediaDate DATE NOT NULL
) ;

CREATE TABLE messages (
  messageId int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  fromId smallint NOT NULL,
  toId smallint NOT NULL,
  messageText varchar(250) NOT NULL,
  dateSent DATE NOT NULL,
  FOREIGN KEY(ToId) REFERENCES student(rollNum),
  FOREIGN KEY(fromId) REFERENCES teacher(teacherID)
) ;

CREATE TABLE transportation (
  transportid int PRIMARY KEY,
  transportDescription varchar(250) ,
  driverName varchar(250),
  transportDriverContact INT NOT NULL,
  transportFare varchar(250) NOT NULL,
  Student smallint,
  FOREIGN KEY(Student) REFERENCES student(rollNum)
) ;

CREATE TABLE payments (
  paymentid int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  Student smallint(250) NOT NULL,
  paymentDescription varchar(250) ,
  paymentAmount float,
  paymentStatus varchar(10),
  paymentDate DATE NOT NULL,
  FOREIGN KEY(Student) REFERENCES student(rollNum),

  constraint chk6 check (paymentStatus = 'paid' or paymentStatus = 'unpaid')

) ;

CREATE TABLE assignments (
  Assignmentid int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  teacherId smallint NOT NULL,
  AssignDescription text,
  AssignFile varchar(250) NOT NULL,
  AssignDeadLine DATE,
  FOREIGN KEY(teacherId) REFERENCES teacher(teacherID)
) ;
CREATE TABLE newsboard (
  newsid int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  newsDescription varchar(250) NOT NULL,
  newsFor varchar(250) NOT NULL,
  newsDate DATE NOT NULL
) ;

create table Lockerlog(Message varchar(90), Dates varchar(30));
create table gradelog(Message varchar(90), Dates varchar(20));

CREATE TABLE FormerStudent (
Msg varchar(90),
rollNum SMALLINT NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
dob DATE NOT NULL,
address VARCHAR(40) NOT NULL,
fatherName VARCHAR(30) NOT NULL,
contactNum VARCHAR(15) NOT NULL,
email VARCHAR(40) NOT NULL,
classID VARCHAR(3) NOT NULL
);
  
  CREATE TABLE FormerTeacher (
  Msg varchar(90),
teacherID SMALLINT NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(40) NOT NULL,
contactNum VARCHAR(15) NOT NULL,
email VARCHAR(40) NOT NULL,
qualification VARCHAR(80) NOT NULL
);
CREATE TABLE Studentlog (
Msg varchar(90),
rollNum SMALLINT NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
dob DATE NOT NULL,
address VARCHAR(40) NOT NULL,
fatherName VARCHAR(30) NOT NULL,
contactNum VARCHAR(15) NOT NULL,
email VARCHAR(40) NOT NULL,
classID VARCHAR(3) NOT NULL
);
  
  CREATE TABLE Teacherlog (
Msg varchar(90),
teacherID smallint NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(40) NOT NULL,
contactNum VARCHAR(15) NOT NULL,
email VARCHAR(40) NOT NULL,
qualification VARCHAR(80) NOT NULL
);

CREATE TRIGGER new_teacher after insert on Teacher for each row
INSERT INTO Teacherlog values(concat("New Record Added at ",NOW(),"by",current_user()), new.teacherID,new.fname,new.lname,new.address,new.contactNum,
new.email,new.qualification);



CREATE TRIGGER new_student after insert on Student for each row
INSERT INTO Studentlog values(concat("New Record Added at ",NOW(),"by",current_user()), new.rollNum,new.fname,new.lname,new.dob,new.address,
new.fatherName,new.contactNum,new.email,new.classID);


CREATE TRIGGER grade_change after update on result for each row
insert into gradelog values(concat("New Record updated:- by",current_user(),"Previous Grade was ",old.obtainedMarks),NOW());

CREATE TRIGGER 	Lockername_change after update on locker for each row
insert into Lockerlog values(concat("New Record updated:- by",current_user()," previous name was ",old.LockerName),NOW());

drop trigger marks_check
DELIMITER //
CREATE TRIGGER marks_check before insert on result for each row 
BEGIN 
IF new.obtainedMarks > maxMarks THEN 
	SET new.obtainedMarks=maxMarks;
end if;
END//



DELIMITER //
CREATE TRIGGER deleted_student after delete 
on Student for each row
BEGIN
insert into FormerStudent values(
CONCAT(("Record deleted on "), NOW(), "by",current_user),
old.rollNum,
old.fname ,
old.lname ,
old.dob ,
old.address,
old.fatherName,
old.contactNum ,
old.email ,
old.classID
);
END//

DELIMITER //
CREATE TRIGGER deleted_teacher after delete 
on Teacher for each row
BEGIN
insert into FormerTeacher values(
CONCAT(("Record deleted on "), NOW(), "by",current_user),
old.teacherID,
old.fname, 
old.lname ,
old.address ,
old.contactNum ,
old.email ,
old.qualification
);
END//






DROP procedure IF EXISTS `get_payments_info`;

DELIMITER $$
USE `school`$$
CREATE PROCEDURE `get_payments_info` ()
BEGIN
select* from payments;
END$$

DELIMITER ;

DROP procedure IF EXISTS `get_classes_info`;

DELIMITER $$
USE `school`$$
CREATE PROCEDURE `get_classes_info` ()
BEGIN
select* from class;
END$$

DELIMITER ;


DROP procedure IF EXISTS `get_subjects_info`;

DELIMITER $$
USE `school`$$
CREATE PROCEDURE `get_subjects_info` ()
BEGIN
select* from subjects;
END$$

DELIMITER ;


DROP procedure IF EXISTS `get_books_info`;

DELIMITER $$
USE `school`$$
CREATE PROCEDURE `get_books_info` ()
BEGIN
select* from booklibrary;
END$$

DELIMITER ;

DROP procedure IF EXISTS `get_students_info`;

DELIMITER $$
USE `school`$$
CREATE PROCEDURE `get_students_info` ()
BEGIN
select* from Student;
END$$

DELIMITER ;

DROP procedure IF EXISTS `get_teachers_info`;

DELIMITER $$
USE `school`$$
CREATE PROCEDURE `get_teachers_info` ()
BEGIN
select* from Teacher;
END$$

DELIMITER ;

DROP procedure IF EXISTS `get_locker_info`;

DELIMITER $$
USE `school`$$
CREATE PROCEDURE `get_locker_info` ()
BEGIN
select* from locker;
END$$

DELIMITER ;

DROP procedure IF EXISTS `get_grades_info`;

DELIMITER $$
USE `school`$$
CREATE PROCEDURE `get_grades_info` ()
BEGIN
select* from result;
END$$

DELIMITER ;

DROP procedure IF EXISTS `get_transport_info`;

DELIMITER $$
USE `school`$$
CREATE PROCEDURE `get_transport_info` ()
BEGIN
select* from transportation;
END$$

DELIMITER ;

DROP procedure IF EXISTS `get_events_info`;

DELIMITER $$
USE `school`$$
CREATE PROCEDURE `get_events_info` ()
BEGIN
select* from events;
END$$

DELIMITER ;





CREATE VIEW class_view as
SELECT classID FROM class;


CREATE VIEW subjects_view as
SELECT subjectID,title FROM subjects;


CREATE VIEW results_view as
SELECT DISTINCT concat(examTitle,' | ',academicYear) FROM result;



CREATE VIEW students_view as 
select * from student;

CREATE VIEW teachers_view as 
select * from teacher;


SET SQL_SAFE_UPDATES = 0;
 