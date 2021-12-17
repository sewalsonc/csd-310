/*
Title:whatabook.init.sql
    Brittany Normandin
    12/14/2021
    Description: WhatABook database initialization script.
*/

CREATE DATABASE whatabook;
-- create whatabook_user and grant them all privileges to whatabook database --
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MYSQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';
-- drop test if user exists --
DROP USER IF EXISTS 'whatabook_user'@'localhost';
-- drop constraints if they exist --
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;
-- drop tables if they exist --
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;
-- create table fields --
CREATE TABLE store (
     store_id INT NOT NULL AUTO_INCREMENT,
     locale VARCHAR(500) NOT NULL,
     PRIMARY KEY(store_id)
     );
CREATE TABLE book (
	book_id INT NOT NULL AUTO_INCREMENT,
	book_name VARCHAR(200) NOT NULL,
	details VARCHAR(500),
	author VARCHAR(200) NOT NULL,
	PRIMARY KEY(book_id)
);
CREATE TABLE user (
	user_id INT NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(75) NOT NULL,
	last_name VARCHAR(75) NOT NULL,
	PRIMARY KEY(user_id)
);
CREATE TABLE wishlist (
	wishlist_id INT NOT NULL AUTO_INCREMENT,
	user_id INT NOT NULL,
	book_id INT NOT NULL,
	PRIMARY KEY(wishlist_id),
	CONSTRAINT fk_book
	FOREIGN KEY(book_id)
	REFERENCES book(book_id),
	CONSTRAINT fk_user
	FOREIGN KEY(user_id)
	REFERENCES user(user_id)
);
/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('1234 whatabook way, Coram NY 11727');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
	VALUES('Amphigorey Also', 'Edward Gorey','Companion volume to Amphigorey and Amphigorey too.');
INSERT INTO book(book_name, author, details)
	VALUES('Hunters of the Lost City', 'Kali Wallace','Packed with shocking twists, frightening monsters, and dark magic.');
INSERT INTO book(book_name, author, details)
	VALUES('Chasing Ghosts', 'Marc Hartzman', 'Take a spirited tour through the supernatural history of America.');
INSERT INTO book(book_name, author, details)
	VALUES('I Whish I had a Wookie', 'Ian Doescher, Tim Budgen', 'Collection of over 75 Star Wars poems.');
INSERT INTO book(book_name, author, details)
	VALUES('Bookish and the Beast', 'Fresh, geeky retelling of Beauty and the Beast.');
INSERT INTO book(book_name, author, details)
	VALUES('Stuff Every Coffee Lover Should Know', 'Candance Rose Rardon', Pocket-sized handbook is the perfect gift for coffee connoisseurs.');
INSERT INTO book(book_name, author, details)
	VALUES('Crystal Clear', 'Jaya Saxena', 'Explores the multi-faceted meanings and history behind eleven popular crystals.');
INSERT INTO book(book_name, author, details)
	VALUES('Secret Santa', 'Andrew Shaffer', 'Fun, festive, and frightening horror-comedy set during the publishing boom of the 80s.');
INSERT INTO book(book_name, author, details)
	VALUES('The Big Book of Mars', 'Marc Hartzman', 'The most comprehensive look at our relationship with Mars - yesterday, today, and tomorrow.');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name)
VALUES('Brittany', 'Normandin');
INSERT INTO user(first_name, last_name)
	VALUES('Taylor', 'Froehlich');
INSERT INTO user(first_name, last_name)
	VALUES('Chris', 'Bayer');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Brittany'), 
        (SELECT book_id FROM book WHERE book_name = 'Secret Santa')
    );
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Taylor'), 
        (SELECT book_id FROM book WHERE book_name = 'Crystal Clear')
    );
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Chris'), 
        (SELECT book_id FROM book WHERE book_name = 'I Whish I had a Wookie')
    );