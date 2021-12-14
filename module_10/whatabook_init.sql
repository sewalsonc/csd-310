/*
    Title: whatabook_init.sql
    Author: Chris Sewalson
    Date: December 5, 2021
    Description: whatabook database initialization script.
*/

-- -- drop test user if exists 
-- DROP USER IF EXISTS 'whatabook_user'@'localhost';


-- -- create whatabook_user and grant them all privileges to the whatabook database 
-- CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8isGreat!';

-- -- grant all privileges to the whatabook database to user whatabook_user on localhost 
-- GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- -- dropping constraints that may exist???
-- ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
-- ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- -- dropping tables
-- DROP TABLE IF EXISTS store;
-- DROP TABLE IF EXISTS book;
-- DROP TABLE IF EXISTS wishlist;
-- DROP TABLE IF EXISTS user;

-- /*
-- Creating tables next
-- */
-- CREATE TABLE store(
--     store_id    INT             NOT NULL    AUTO_INCREMENT,
--     locale      VARCHAR(500)    NOT NULL,
--     PRIMARY KEY(store_id)
-- );

-- CREATE TABLE book(
--     book_id     INT             NOT NULL    AUTO_INCREMENT,
--     book_name   VARCHAR(200)    NOT NULL,
--     author      VARCHAR(200)    NOT NULL,
--     details     VARCHAR(500),
--     PRIMARY KEY(book_id)
-- );

-- CREATE TABLE user(
--     user_id     INT             NOT NULL    AUTO_INCREMENT,
--     first_name  VARCHAR(75)     NOT NULL,
--     last_name   VARCHAR(75)     NOT NULL,
--     PRIMARY KEY(user_id)
-- );

-- CREATE TABLE wishlist(
--     wishlist_id INT             NOT NULL    AUTO_INCREMENT,
--     user_id     INT             NOT NULL,
--     book_id     INT             NOT NULL,
--     PRIMARY KEY(wishlist_id),
--     CONSTRAINT fk_book
--     FOREIGN KEY(book_id)
--         REFERENCES book(book_id),
--     CONSTRAINT fk_user
--     FOREIGN KEY(user_id)
--         REFERENCES user(user_id)
-- );
-- /*
--     inserting store information 
-- */
INSERT INTO store(locale)
    VALUES('4578 Helen St., Sioux City IA, 51106');

/*
    inserting books 
*/
INSERT INTO book(book_name, author, details)
    VALUES('Gypsys Road: Tale of Winter', 'J. Ralph', 'First part of Gypsy Trilogy');

INSERT INTO book(book_name, author, details)
    VALUES('Gypsys Road: Taken Back to Dawn', 'J. Ralph', 'Second part of Gypsy Trilogy');

INSERT INTO book(book_name, author, details)
    VALUES('Gypsys Road: Follow the End', 'J. Ralph', 'Third part of Gypsy Trilogy');

INSERT INTO book(book_name, author, details)
    VALUES('Born of Fear', 'Perry Winside', 'Middle eastern thriller');

INSERT INTO book(book_name, author)
    VALUES('Fourth Race of Crackhour', 'Forrest Kilder');

INSERT INTO book(book_name, author)
    VALUES("Pride of American Tradition", 'Plasus Driesen');

INSERT INTO book(book_name, author, details)
    VALUES('As of Late', 'Taylor Howitz', 'Mystery and suspense');

INSERT INTO book(book_name, author)
    VALUES('Treadwells Fate', 'Forrest Kilder');

INSERT INTO book(book_name, author)
    VALUES('Blood Runs Deep', 'J.K. Ifonly');

/*
    insert users
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Chris', 'Sewalson');

INSERT INTO user(first_name, last_name)
    VALUES('Frank', 'Litny');

INSERT INTO user(first_name, last_name)
    VALUES('Corey', 'Parder');

/*
    insert wishlist users and books
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Chris'), 
        (SELECT book_id FROM book WHERE book_name = 'Blood Runs Deep')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Frank'),
        (SELECT book_id FROM book WHERE book_name = 'Treadwells Fate')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Corey'),
        (SELECT book_id FROM book WHERE book_name = 'As of Late')
    );