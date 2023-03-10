SELECT * FROM python_connector.registration_data;

use python_connector;

create table Account (Name varchar(10), Address varchar(20),  Aadhar int, Mobile_no int);

show tables;





select * from amount2;
drop table account;


Create table Beneficiaries (AccNo int, Beneficiary varchar(10), Transfer_amount int);

drop table amount;

drop table account1;

create table ACCOUNT( Name varchar(10), AccNo int, Address varchar(10), ContactNo varchar(10), OpeningBal int);

Create table AMOUNT( Name varchar(10), AccNo int, Balance int);

select * from ACCOUNT;

select * from AMOUNT;


select * from Registration;

select * from Beneficiaries;
delete from Registration where User_id =1234;


Create table Credit_Cards (AccNo int, Card_no int, Pin varchar(10), Cvv int);

Create table Debit_Cards (AccNo int, Card_no int, Pin varchar(10), Cvv int);


select * from Credit_Cards;


create table Registration(User_id int, Passwordd varchar(10));