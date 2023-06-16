--Part 1
SELECT * FROM film WHERE rental_duration > 4;

--part 2
SELECT * FROM film WHERE rental_duration > 2 AND  rental_duration < 5;

--part 3
SELECT * FROM film WHERE rental_duration > 4 ORDER BY title ASC;
SELECT * FROM film WHERE rental_duration > 4 ORDER BY title DESC;

SELECT * FROM film WHERE rental_duration > 4 ORDER BY rental_duration ASC;
SELECT * FROM film WHERE rental_duration > 4 ORDER BY rental_duration DESC;

SELECT * FROM film WHERE rental_duration > 4 ORDER BY last_update ASC;
SELECT * FROM film WHERE rental_duration > 4 ORDER BY last_update DESC;

SELECT * FROM film WHERE rental_duration > 2 AND  rental_duration < 5 ORDER BY title ASC;
SELECT * FROM film WHERE rental_duration > 2 AND  rental_duration < 5 ORDER BY title DESC;

SELECT * FROM film WHERE rental_duration > 2 AND  rental_duration < 5 ORDER BY rental_duration ASC;
SELECT * FROM film WHERE rental_duration > 2 AND  rental_duration < 5 ORDER BY rental_duration DESC;

SELECT * FROM film WHERE rental_duration > 2 AND  rental_duration < 5 ORDER BY last_update ASC;
SELECT * FROM film WHERE rental_duration > 2 AND  rental_duration < 5 ORDER BY last_update DESC;

--part4
SELECT MIN(length) FROM film;
SELECT MAX(length) FROM film;
SELECT AVG(length) FROM film;