# E-dhamma Backend

> A Python Django project.

## Purpose

This application provides the backend for E-dhamma projects such as [Pali-Estonian Dictionary Web Application](https://github.com/e-dhamma/Pali-Estonian-dictionary-web-application).

## Installation

1. On your computer go to the directory where you want the project to be located at.
1. Clone the project

       git clone https://github.com/e-dhamma/e-dhamma-backend

1. Create  and activate virtualenv

       cd e-dhamma-backend
       virtualenv venv
       . ./venv/scripts/activate # Git Bash on Windows
       . ./venv/bin/activate # On Linux

1. Install dependencies

       pip install --requirement=src/requirements.txt

1. Run Django development server

       ./src/manage.py runserver
