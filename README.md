<div id="top"></div>

[Frontend][frontend-url]
[Heroku][herokuapp-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Ada Book Club</h3>

  <p align="center">
    This is the backend for Ada Book Club
    
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This is the backend for our capstone project, Ada Book Club. Part of our learning goal was to learn how to implement Django.

The aim of our web app is to be a hub for book lovers to create or join groups based on what book they’re reading. Our MVP included progress tracking, searching books through Google Books API, and posting to the forum.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Django](https://djangoproject.org/)
* [Python](https://python.org/)
* [PostgreSQL](https://www.postgreslq.org)


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Local Database Setup
1. Log in to Postgres
	```sh
	psql -U postgres
	```
2. Create database
	```sh
	CREATE DATABASE adabookclub;	
    CREATE USER django WITH PASSWORD 'password';

   	GRANT ALL PRIVILEGES ON DATABASE adabookclub TO django;
	```
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mcatcruz/ada-capstone-book-club.git
   ```
2. Create a virtual environment
	```sh
   	python3 -m venv venv
	```
4. Install dependencies inside the virtual environment
	```sh
   	pip3 install -r requirements.txt
  	```
5. Create a .env file. Include `.env` in .gitignore file
   ```sh
   touch .env
   ```
6. Store `SECRET_KEY` inside .env file

### Run the Server
	```sh
	python3 manage.py runserver
	```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[frontend-url]: https://github.com/emilycolonq/ada-capstone-front-book-club
[herokuapp-url]: https://ada-capstone-book-club.herokuapp.com/adabookclub/
