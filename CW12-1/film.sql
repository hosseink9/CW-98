--part 1
SELECT film.title,film.release_year,(category.name) AS category FROM film
INNER JOIN film_category ON film_category.film_id=film.film_id
INNER JOIN category ON category.category_id = film_category.category_id;
