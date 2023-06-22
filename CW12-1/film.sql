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

--part 6
SELECT customer.customer_id,customer.first_name,customer.last_name,(rental.return_date - rental.rental_date) AS rental_days, film.title FROM customer
INNER JOIN rental ON rental.customer_id = customer.customer_id
INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
INNER JOIN film ON film.film_id = inventory.inventory_id;


--part 7

select * from film
where film.length > (select avg(length) from film);