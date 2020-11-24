USE MASTER
CREATE DATABASE CONTACT_BOOK

USE CONTACT_BOOK
GO


CREATE TABLE PEOPLE
(
    id      INT           IDENTITY PRIMARY KEY,
    name    NVARCHAR(100) NOT NULL DEFAULT N'Unknown name',
    address NVARCHAR(100) NOT NULL DEFAULT N'Unknown address',
    phone   NVARCHAR(100) NOT NULL DEFAULT N'Unknown phone',
    email   NVARCHAR(100) NOT NULL DEFAULT N'Unknown email',
)

INSERT PEOPLE
    (name,address,phone,email)
VALUES('Phat', '154 GV', '0944651790', '19521992@gm.uit.vn' )

INSERT PEOPLE
    (name,address,phone,email)
VALUES('Quy', '108 Q9', '0935589947', '19522108@gm.uit.vn' )

SELECT *
FROM PEOPLE

SELECT COUNT(*)
FROM PEOPLE
WHERE PEOPLE.name='Phat'