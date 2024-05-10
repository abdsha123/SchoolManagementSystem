USE school;

INSERT INTO teacher
VALUES(101,"Arthur","Denise","P.O. Box 323, 1525 Dolor Rd.",0379-5447800, "artuhrdeniseutmolestiein.net","MS Mathematics"),
(102,"Cassandra","Claire","P.O. Box 326, 817 Eu, St.",0336-9585029,"cassandraclaire@Etiamvestibulummassa.ca","BS Calculus"),
(103,"Travis","Ignacia","360-7033 Est, Avenue",	0352-2271159,"pede@euismodetcommodo.org)","MS Physics"),
(104,"Alvin","Tanisha",	"Ap #171-5550 Mauris St.",0350-5158789,"facilisis.non.bibendum@Donec.org","MSc Medical Physics"),
(105,"Jenette","Ulric","Ap #397-2672 Phasellus Street",0323-8277731,"interdum.enim.non@idliberoDonec.ca","MA English"),
(106,"Maria","Anders","Obere Str. 57",0323-8457231,"mariaAnders@idliberoDonec.ca","MA English"),
(107,"Thomas","Hardy","120 Hanover Sq.",0313-6253251,"hardyboi@raclai.edu","MA Urdu"),
(110,"Rosella","Kuhlman","13641 Jacobson Plaza",0312-6243251,"crystal.howe@example.com","MA Urdu"),
(115,"Brent","Koss","18848 Jaida Glen Apt. 469",0323-2213252,"samir05@example.net","Msc Geography"),
(116,"Sheila","Jaskolski","65251 Koch Junction",0313-4252151,"nathan.bashirian@example.net","Msc Architecture"),
(117,"Ryley","Romaguera","370 Hahn Rest Apt. 387",0324-1213253,"heller.devonte@example.org","Msc Computer Science"),
(118,"Coby","Torp","049 Daugherty Wells",0323-6252154,"bayer.arlene@example.org","Msc Computer Science");



INSERT INTO class
VALUES("6A",101),
("6B",104);



INSERT INTO subjects
VALUES(188,"Mathematics", "Mathematics for Middle School"),
(777,"Science", "General Science for Middle Schoool"),
(111,"English", "Middle School English reading and poetry"),
(117,"Urdu","Middle School Urdu reading and poetry"),
(132,"Social Studies","History and Geography for middle school"),
(169,"Computer Science","History and basics of computers");


INSERT INTO room
VALUES(1,"ClassRoom","BLOCK B Ground Floor",40),
(2,"ClassRoom","BLOCK B Ground Floor",40),
(3,"ClassRoom","BLOCK B Ground Floor",35),
(4,"ClassRoom","BLOCK A Ground Floor",35),
(5,"ClassRoom","BLOCK A First Floor",40),
(6,"ClassRoom","BLOCK A First Floor",45),
(7,"ClassRoom","BLOCK B First Floor",35),
(8,"ClassRoom","BLOCK B First Floor",45),
(9,"ClassRoom","BLOCK B First Floor",45),
(10,"ClassRoom","BLOCK A First Floor",45),
(11,"Science Lab","BLOCK A Second Floor",60),
(12,"Computer Lab","BLOCK A Second Floor",60);

INSERT INTO teaches
VALUES("6A",188,101),("6A",777,103), ("6A",111,105), ("6A",117,107), ("6A",132,115), ("6A",169,117),
("6B",188,102),("6B",777,103), ("6B",111,106), ("6B",117,110), ("6B",132,115), ("6B",169,118);

INSERT INTO Student 
VALUES (11, 'Roma', 'Strosin', '1987-08-27', '4565 Odie Road Suite 966 Valentinport, R', 'Birdie Runte', '0311-3124568', 'esteban.jast@example.org', "6A"),
(12, 'Gerson', 'DuBuque', '1984-10-20', '7501 Howell Ridges Apt. 726 New Sanfordv', 'Kari Wilderman', '0323-58292390', 'robbie75@example.org',  "6A"),
(13, 'Rowan', 'Muller', '1989-10-23', '52224 Crawford Pike Suite 721 Chazcheste', 'Rosamond Roob',  '0123-1235125', 'darrion68@example.org',  "6A"),
(14, 'Novella', 'Turcotte', '1973-04-13', '0499 Amy Court Suite 262 Heberport TX 6', 'lexie Wisoky', '0322-2235328', 'ruben06@example.com', "6A"),
(15, 'Abby', 'Johnston', '2002-12-16', '9288 Christine Causeway New Darrionstad,', 'Arden Osinski', '0322-5115532', 'zblick@example.com', "6A"),
(21, 'Destiny', 'Terry', '1983-10-25', '01378 Glover Creek', 'Meda Durgan','0376-7825625', 'rowena.cremin@example.org', "6A"),
(22, 'Mireille', 'Price', '1996-03-09', '0463 Helene Wall Apt. 705', 'Alba Kuphal','0315-7746529', 'kurt74@example.com', "6A"),
(23, 'Frida', 'Hahn', '2003-01-08', '2104 Hoppe Views', 'Prof. Emilie Mueller','0314-2826703', 'julie44@example.com', "6A"),
(24, 'Timmy', 'Pouros', '1990-05-06', '749 Heidenreich Roads', 'Jeanette West','0372-2918521', 'nikolaus.clemens@example.org', "6A"),
(25, 'Jacynthe', 'Ebert', '1978-07-20', '9206 Lubowitz Glens Suite 551', 'Domingo Mayer','0371-1650253', 'wiley.bartoletti@example.com', "6A"),
(26, 'Grant', 'Barton', '1990-06-16', '4800 Darien Circle', 'Carole Skiles','0358-0236046', 'dameon.zieme@example.org', "6B"),
(27, 'Estel', 'Pfeffer', '1988-12-06', '654 Schiller Forges', 'Andre Kub','0315-5649717', 'epurdy@example.com', "6B"),
(28, 'Rowan', 'Conner', '1988-06-19', '3675 Huels Ville', 'Mrs. Marcella Sanford','0314-1276853', 'zkuhlman@example.org',"6B"),
(29, 'Kellie', 'Amore', '1987-08-03', '7080 Schumm Cliff', 'Reinhold Bosco','0311-2621457', 'kertzmann.cedrick@example.org', "6B"),
(30, 'Viola', 'Heaney', '1976-06-02', '4714 Demarco Causeway', 'Johnathan Green','0326-8472741', 'farrell.valerie@example.org', "6B"),
(16, 'Hubert', 'Stokes', '2020-06-14', '60183 Strosin Shoal Suite 936 East Jazmi', 'Nico McKenzie', '0324-1122112', 'antwan32@example.org', "6B"),
(17, 'Jeff', 'Durgan', '2008-04-05', '1106 Beier Brooks West Dorcasland, NV 62', 'Fernando Huels', '0322-1234471', 'deborah62@example.com', "6B"),
(18, 'Yoshiko', 'McKenzie', '1978-05-22', '6333 Damian Ridge Eulahville, MT 95419-7', 'Gladys Ritchie III','0322-1234471', 'alessia.treutel@example.com', "6B"),
(19, 'Amely', 'Rodriguez', '1974-02-08', '038 Sterling Groves North Roberta, MA 79', 'Lola Bogan', '0322-5785321', 'julia62@example.org', "6B"),
(20, 'Erna', 'Wilderman', '1995-03-07', '8614 Pollich Ville', 'Angelo Frami', '0303-4770408', 'norwood81@example.net', "6B");




INSERT INTO result
VALUES	
("First Term",2019,11,188,100,87),("First Term",2019,12,188,100,83),("First Term",2019,13,188,100,97),("First Term",2019,14,188,100,86),("First Term",2019,15,188,100,67),
("First Term",2019,11,777,100,82),("First Term",2019,12,777,100,77),("First Term",2019,13,777,100,77),("First Term",2019,14,777,100,68),("First Term",2019,15,777,100,64),
("First Term",2019,11,111,100,81),("First Term",2019,12,111,100,71),("First Term",2019,13,111,100,61),("First Term",2019,14,111,100,74),("First Term",2019,15,111,100,82),
("First Term",2019,11,117,100,85),("First Term",2019,12,117,100,84),("First Term",2019,13,117,100,67),("First Term",2019,14,117,100,57),("First Term",2019,15,117,100,79),
("First Term",2019,11,132,100,85),("First Term",2019,12,132,100,71),("First Term",2019,13,132,100,77),("First Term",2019,14,132,100,72),("First Term",2019,15,132,100,59),
("First Term",2019,11,169,100,87),("First Term",2019,12,169,100,87),("First Term",2019,13,169,100,81),("First Term",2019,14,169,100,71),("First Term",2019,15,169,100,85),

("First Term",2019,16,188,100,87),("First Term",2019,17,188,100,63),("First Term",2019,18,188,100,99),("First Term",2019,19,188,100,81),("First Term",2019,20,188,100,67),
("First Term",2019,16,777,100,72),("First Term",2019,17,777,100,67),("First Term",2019,18,777,100,79),("First Term",2019,19,777,100,60),("First Term",2019,20,777,100,64),
("First Term",2019,16,111,100,71),("First Term",2019,17,111,100,61),("First Term",2019,18,111,100,69),("First Term",2019,19,111,100,72),("First Term",2019,20,111,100,62),
("First Term",2019,16,117,100,72),("First Term",2019,17,117,100,84),("First Term",2019,18,117,100,86),("First Term",2019,19,117,100,50),("First Term",2019,20,117,100,72),
("First Term",2019,16,132,100,82),("First Term",2019,17,132,100,74),("First Term",2019,18,132,100,87),("First Term",2019,19,132,100,74),("First Term",2019,20,132,100,52),
("First Term",2019,16,169,100,87),("First Term",2019,17,169,100,87),("First Term",2019,18,169,100,88),("First Term",2019,19,169,100,70),("First Term",2019,20,169,100,81),

("First Term",2019,11,188,100,87),("First Term",2019,12,188,100,83),("First Term",2019,13,188,100,97),("First Term",2019,14,188,100,86),("First Term",2019,15,188,100,67),
("First Term",2019,11,777,100,82),("First Term",2019,12,777,100,77),("First Term",2019,13,777,100,77),("First Term",2019,14,777,100,68),("First Term",2019,15,777,100,64),
("First Term",2019,11,111,100,81),("First Term",2019,12,111,100,71),("First Term",2019,13,111,100,61),("First Term",2019,14,111,100,74),("First Term",2019,15,111,100,82),
("First Term",2019,11,117,100,85),("First Term",2019,12,117,100,84),("First Term",2019,13,117,100,67),("First Term",2019,14,117,100,57),("First Term",2019,15,117,100,79),
("First Term",2019,11,132,100,85),("First Term",2019,12,132,100,71),("First Term",2019,13,132,100,77),("First Term",2019,14,132,100,72),("First Term",2019,15,132,100,59),
("First Term",2019,11,169,100,87),("First Term",2019,12,169,100,87),("First Term",2019,13,169,100,81),("First Term",2019,14,169,100,71),("First Term",2019,15,169,100,85),

("First Term",2019,16,188,100,87),("First Term",2019,17,188,100,63),("First Term",2019,18,188,100,99),("First Term",2019,19,188,100,81),("First Term",2019,20,188,100,67),
("First Term",2019,16,777,100,72),("First Term",2019,17,777,100,67),("First Term",2019,18,777,100,79),("First Term",2019,19,777,100,60),("First Term",2019,20,777,100,64),
("First Term",2019,16,111,100,71),("First Term",2019,17,111,100,61),("First Term",2019,18,111,100,69),("First Term",2019,19,111,100,72),("First Term",2019,20,111,100,62),
("First Term",2019,16,117,100,72),("First Term",2019,17,117,100,84),("First Term",2019,18,117,100,86),("First Term",2019,19,117,100,50),("First Term",2019,20,117,100,72),
("First Term",2019,16,132,100,82),("First Term",2019,17,132,100,74),("First Term",2019,18,132,100,87),("First Term",2019,19,132,100,74),("First Term",2019,20,132,100,52),
("First Term",2019,16,169,100,87),("First Term",2019,17,169,100,87),("First Term",2019,18,169,100,88),("First Term",2019,19,169,100,70),("First Term",2019,20,169,100,81),

("First Term",2019,21,188,100,87),("First Term",2019,22,188,100,83),("First Term",2019,23,188,100,87),("First Term",2019,24,188,100,86),("First Term",2019,25,188,100,67),
("First Term",2019,21,777,100,82),("First Term",2019,22,777,100,72),("First Term",2019,23,777,100,87),("First Term",2019,24,777,100,68),("First Term",2019,25,777,100,74),
("First Term",2019,21,111,100,81),("First Term",2019,22,111,100,72),("First Term",2019,23,111,100,81),("First Term",2019,24,111,100,64),("First Term",2019,25,111,100,72),
("First Term",2019,21,117,100,85),("First Term",2019,22,117,100,82),("First Term",2019,23,117,100,87),("First Term",2019,24,117,100,67),("First Term",2019,25,117,100,79),
("First Term",2019,21,132,100,85),("First Term",2019,22,132,100,71),("First Term",2019,23,132,100,77),("First Term",2019,24,132,100,62),("First Term",2019,25,132,100,79),
("First Term",2019,21,169,100,87),("First Term",2019,22,169,100,87),("First Term",2019,23,169,100,81),("First Term",2019,24,169,100,61),("First Term",2019,25,169,100,85),

("First Term",2019,26,188,100,87),("First Term",2019,27,188,100,63),("First Term",2019,28,188,100,99),("First Term",2019,29,188,100,81),("First Term",2019,30,188,100,67),
("First Term",2019,26,777,100,72),("First Term",2019,27,777,100,67),("First Term",2019,28,777,100,79),("First Term",2019,29,777,100,60),("First Term",2019,30,777,100,64),
("First Term",2019,26,111,100,72),("First Term",2019,27,111,100,61),("First Term",2019,28,111,100,79),("First Term",2019,29,111,100,72),("First Term",2019,30,111,100,62),
("First Term",2019,26,117,100,72),("First Term",2019,27,117,100,84),("First Term",2019,28,117,100,76),("First Term",2019,29,117,100,50),("First Term",2019,30,117,100,72),
("First Term",2019,26,132,100,82),("First Term",2019,27,132,100,74),("First Term",2019,28,132,100,77),("First Term",2019,29,132,100,74),("First Term",2019,30,132,100,52),
("First Term",2019,26,169,100,87),("First Term",2019,27,169,100,87),("First Term",2019,28,169,100,88),("First Term",2019,29,169,100,70),("First Term",2019,30,169,100,81);

;

INSERT INTO meeting
VALUE 
(1,"Monday","6A",1,188),(1,"Tuesday","6A",3,188),(1,"Wednesday","6A",3,188),(1,"Thursday","6A",1,777),(1,"Friday","6A",1,169),
(2,"Monday","6A",1,188),(2,"Tuesday","6A",3,188),(2,"Wednesday","6A",5,169),(2,"Thursday","6A",1,132),(2,"Friday","6A",1,169),
(3,"Monday","6A",3,169),(3,"Tuesday","6A",1,169),(3,"Wednesday","6A",3,132),(3,"Thursday","6A",3,169),(3,"Friday","6A",5,111),
(4,"Monday","6A",6,111),(4,"Tuesday","6A",3,111),(4,"Wednesday","6A",3,111),(4,"Thursday","6A",5,111),(4,"Friday","6A",1,111),
(5,"Monday","6A",6,777),(5,"Tuesday","6A",7,777),(5,"Wednesday","6A",5,777),(5,"Thursday","6A",1,188),(5,"Friday","6A",5,777),
(6,"Monday","6A",1,132),(6,"Tuesday","6A",7,132),(6,"Wednesday","6A",3,132),(6,"Thursday","6A",1,188),(6,"Friday","6A",3,132),

(1,"Monday","6B",4,169),(1,"Tuesday","6B",4,111),(1,"Wednesday","6B",4,111),(1,"Thursday","6B",3,188),(1,"Friday","6B",4,169),
(2,"Monday","6B",2,169),(2,"Tuesday","6B",4,111),(2,"Wednesday","6B",2,777),(2,"Thursday","6B",2,188),(2,"Friday","6B",4,169),
(3,"Monday","6B",2,111),(3,"Tuesday","6B",6,777),(3,"Wednesday","6B",2,169),(3,"Thursday","6B",2,169),(3,"Friday","6B",2,111),
(4,"Monday","6B",2,777),(4,"Tuesday","6B",6,132),(4,"Wednesday","6B",6,111),(4,"Thursday","6B",3,111),(4,"Friday","6B",6,111),
(5,"Monday","6B",4,132),(5,"Tuesday","6B",8,188),(5,"Wednesday","6B",6,777),(5,"Thursday","6B",5,777),(5,"Friday","6B",6,777),
(6,"Monday","6B",4,188),(6,"Tuesday","6B",8,188),(6,"Wednesday","6B",8,132),(6,"Thursday","6B",5,132),(6,"Friday","6B",7,132);


insert into locker values
(1,"Locker1",20),
(2,"Locker2",29),
(3,"Locker3",19),
(4,"Locker4",11),
(5,"Locker5",14);





insert into booklibrary values
(1,"The Black Forest","Novel","Tom Phillip",200,"2022-08-21",11),
(2,"The Old Man","Novel","Bill Larry",500,"2022-08-31",20),
(3,"Advanced Mathematics","Science","Kyle Walker",800,"2022-11-21",29),
(4,"The Big Bang","Fiction","Lee Omega",1000,"2022-10-22",24);

insert into transportation values
(1,"Bus","Kenny",33258493,2500,11),
(2,"Van","Abraham",021849202,5000,22),
(3,"E-Van","Alex",293920292,18000,29);

insert into newsboard values
(1,"Exams are starting next month","Students and Teachers","2022-08-21");

insert into messages values
(1,104,29,"Come to my Office!","2022-08-21");

insert into events values
(1,"Sports Gala", "Everyone","Main Ground","2023-01-01");

insert into payments values
(1,29, "Dues for the semester",500000,"unpaid","2022-08-19");

