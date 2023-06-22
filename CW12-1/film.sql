--part 1
SELECT film.title,film.release_year,(category.name) AS category FROM film
INNER JOIN film_category ON film_category.film_id=film.film_id
INNER JOIN category ON category.category_id = film_category.category_id;

--Part 2 
SELECT film.title,film.release_year,(category.name) AS category FROM film
INNER JOIN film_category ON film_category.film_id=film.film_id
INNER JOIN category ON category.category_id = film_category.category_id
WHERE category.name IN ('Action','Comedy','Family');

--part 3
SELECT category,count(*) FROM film
INNER JOIN film_category ON film_category.film_id=film.film_id
INNER JOIN category ON category.category_id = film_category.category_id 
GROUP BY category;

--part 4
SELECT category,count(*) FROM film
INNER JOIN film_category ON film_category.film_id=film.film_id
INNER JOIN category ON category.category_id = film_category.category_id 
GROUP BY category HAVING count(*) BETWEEN '60' AND '68' ;

--part 5
SELECT film.title,language.name,category.name FROM language
INNER JOIN film ON film.language_id = language.language_id
INNER JOIN film_category ON film_category.film_id=film.film_id
INNER JOIN category ON category.category_id = film_category.category_id;


