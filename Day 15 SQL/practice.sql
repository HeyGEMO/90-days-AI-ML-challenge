create database company;
use company;
create table payment(customer_id int primary key,
customer varchar(50),
mode varchar(50),
city varchar(50)
);
insert into payment(customer_id,customer,mode,city) values
(101,'olivia barrett','netbanking','portland'),
(102,'ethan sinclair', 'credit card','miami'),
(103,'maya hemandez','credit card','seattle'),
(104,'liam donovan','netbanking','denver'),
(105,'sophia nguyen','credit card','new orlins'),
(106,'caleb foster','debit card','mineapolis'),
(107,'ava patel','debit card','pheonix'),
(108,'lucas carter','netbanking','boston'),
(109,'isabella martinez','netbanking','nashvile'),
(110,'jackson brooks','credit card','boston');

select mode, count(customer) from payment group by mode;
