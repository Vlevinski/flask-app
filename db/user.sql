CREATE DATABASE notes;
use notes;

CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `email` varchar(150) NOT NULL,
  `phone` int unsigned NOT NULL,
  `address` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into `user`(`id`,`name`,`email`,`phone`,`address`) values
(1,'Nick Parson','nick@gmail.com',12345678,'None'),
(2,'Ralph Pen','ralph@gmail.com',12398765,'Remote'),
(3,'Hellen Duck','hellenl@gmail.com',12356789,'Next door');
