Database Management Scripts Readme
This repository contains a set of scripts designed to interact with a MySQL database, particularly focusing on tasks related to user privileges, database creation, table creation, and data retrieval. Each script is documented briefly below.

Task 0: My Privileges!
Script: 0-my_privileges.sql
Description: This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your MySQL server running locally (localhost).
Task 1: Read User
Script: 1-read_user.sql
Description: This script creates the database hbtn_0d_2 and the user user_0d_2. user_0d_2 is granted only the SELECT privilege in the hbtn_0d_2 database. If the database or user already exists, the script does not fail.
Task 3: Always a Name
Script: 3-force_name.sql
Description: This script creates the table force_name with columns id (INT) and name (VARCHAR(256)) on your MySQL server. The name column is set to not allow null values. The database name will be passed as an argument to the mysql command. If the table force_name already exists, the script does not fail.
Task 4: ID Can't Be Null
Script: 4-id_not_null.sql
Description: This script creates the table id_not_null with columns id (INT with a default value of 1) and name (VARCHAR(256)) on your MySQL server. The database name will be passed as an argument to the mysql command. If the table id_not_null already exists, the script does not fail.
Task 5: Unique ID
Script: 5-unique_id.sql
Description: This script creates the table unique_id with columns id (INT with a default value of 1 and must be unique) and name (VARCHAR(256)) on your MySQL server. The database name will be passed as an argument to the mysql command. If the table unique_id already exists, the script does not fail.
Task 6: States Table
Script: 6-states_table.sql
Description: This script creates the database hbtn_0d_usa and the table states in the hbtn_0d_usa database. The states table includes columns id (INT, unique, auto-generated, not null, primary key) and name (VARCHAR(256) can't be null). If the database or table already exists, the script does not fail.
Task 7: Cities Table
Script: 7-cities_table.sql
Description: This script creates the database hbtn_0d_usa and the table cities in the hbtn_0d_usa database. The cities table includes columns id (INT, unique, auto-generated, not null, primary key), state_id (INT, not null, foreign key referencing id of the states table), and name (VARCHAR(256) can't be null). If the database or table already exists, the script does not fail.
Task 8: Cities of California
Script: 8-cities_of_california.sql
Description: This script lists all the cities of California that can be found in the hbtn_0d_usa database. Results are sorted in ascending order by cities.id. The JOIN keyword is not allowed.
Task 9: Cities by States
Script: 9-cities_by_states.sql
Description: This script lists all cities contained in the hbtn_0d_usa database, displaying each record as cities.id - cities.name - states.name. Results are sorted in ascending order by cities.id, and it uses only one SELECT statement.
Task 10: Genre ID by Show
Script: 10-genre_id_by_show.sql
Description: This script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked. Each record displays tv_shows.title - tv_show_genres.genre_id, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id. Only one SELECT statement is allowed.
Task 11: Genre ID for All Shows
Script: 11-genre_id_all_shows.sql
Description: This script lists all shows contained in the hbtn_0d_tvshows database. Each record displays tv_shows.title - tv_show_genres.genre_id. Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id. If a show doesn't have a genre, NULL is displayed.
Task 12: No Genre
Script: 12-no_genre.sql
Description: This script lists all shows contained in hbtn_0d_tvshows without a genre linked. Each record displays tv_shows.title - tv_show_genres.genre_id, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id. Only one SELECT statement is allowed.
Task 14: My Genres
Script: 14-my_genres.sql
Description: This script lists all genres of the show Dexter in the hbtn_0d_tvshows database. Each record displays tv_genres.name, sorted in ascending order by genre name.
Task 15: Only Comedy
Script: 15-only_comedy.sql
Description: This script lists all Comedy shows in the hbtn_0d_tvshows database. Each record displays tv_shows.title, sorted in ascending order by the show title.
Task 16: List Shows and Genres
Script: 16-list_shows_and_genres.sql
Description: This script lists all shows and all genres linked to those shows in the hbtn_0d_tvshows database. If a show doesn't have a genre, NULL is displayed in the genre column. Each record displays tv_shows.title - tv_genres.name, sorted in ascending order by the show title and genre name



Database Management Scripts Readme (Advanced)
This repository contains a set of advanced SQL scripts for managing a MySQL database, particularly focusing on tasks related to genres, show ratings, and data retrieval. Each script is documented briefly below.

Task 17: Not My Genre
Script: 100-not_my_genres.sql
Description: This script uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter. The tv_shows table contains only one record where title = Dexter. Each record displayed is the name of a genre. Results are sorted in ascending order by the genre name, and it uses a maximum of two SELECT statements.
Task 18: No Comedy Tonight!
Script: 101-not_a_comedy.sql
Description: This script lists all shows without the genre Comedy in the hbtn_0d_tvshows database. The tv_genres table contains only one record where name = Comedy. Each record displayed is the title of a show. Results are sorted in ascending order by the show title, and it uses a maximum of two SELECT statements.
Task 19: Rotten Tomatoes
Script: 102-rating_shows.sql
Description: This script imports the hbtn_0d_tvshows_rate database dump and lists all shows from this database by their rating. Each record displayed includes the show's title and rating sum. Results are sorted in descending order by the rating, and it uses only one SELECT statement.
Task 20: Best Genre
Script: 103-rating_genres.sql
Description: This script imports the hbtn_0d_tvshows_rate database dump and lists all genres in the hbtn_0d_tvshows_rate database by their rating. Each record displayed includes the genre's name and rating sum. Results are sorted in descending order by the rating, and it uses only one SELECT statement.
These advanced scripts provide valuable insights into genres, ratings, and data analysis in the context of a TV show database. You can use them to explore and analyze data related to TV shows and genres.




.
