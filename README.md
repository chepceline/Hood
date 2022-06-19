## Description

celhood is a web app that allow one to choose their nieghbourhood they would like to live in. the people get to know the businesses available in their hood and also updates of information. They also get to see their neighbours. 
## Features

The home page allows users to see the signup page where they signup to use the application:
User can update their profile, change neighborhood, post a communication, post a business.
Users can also see the emergency contancts in that neighborhood and neighbours

## View Live Site here

https://celhood.herokuapp.com/

## Technologies Used

- Python 3.8
- Django MVC framework
- HTML, CSS and Bootstrap
- JavaScript
- Postgressql
- Heroku
## Prerequisite

The celhood project requires a prerequisite understanding of the following:

Django Framework
Python3.8
Postgres
Python virtualenv

## Setup and installation

# Clone the Repo from

https://github.com/chepceline/Hood.git

# Activate virtual environment

Activate virtual environment using python3.8 as default handler virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate

# Install dependancies

Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

# Create the Database

- psql
- CREATE DATABASE database name;
# .env file

Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = '<database_name >'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

# Run initial Migration

python3.8 manage.py makemigrations 
python3.8 manage.py migrate

# Run the app

python3.8 manage.py runserver
Open terminal on localhost:8000

# Contributors
- Damaris Chepchirchir

# Contact Information
chepceline25@gmail.com