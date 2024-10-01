# Project Setup Guide

This guide will help you set up the project on your local machine. Follow the steps below to get started.

## Prerequisites

Make sure you have the following installed on your system:
- Git
- Python (version specified in the project)
- Pipenv

## Setup Instructions

1. **Clone the Repository**  
   Use the following command to clone the repository:
   ```bash
   git clone https://github.com/Hasib105/EMS.git
   ```

2. **Activate the Virtual Environment**  
   Navigate into the project directory and activate the environment:
   ```bash
   pipenv shell
   ```
   
3. **Install Dependencies**  
   Install the required dependencies using Pipenv:
   ```bash
   pipenv install
   ```
   
4. **Run Migrations**  
   Apply the database migrations with the following command:
   ```bash
   python manage.py migrate
   ```
   
5. **Seed the Departments**  
   Populate the database with initial department data:
   ```bash
   python manage.py seed_departments
   ```

6. **Seed Achievements**  
   Populate the database with initial department data:
   ```bash
   python manage.py seed_achievements
   ```
   
6. **Run the Server**  
  Start the development server:
   ```bash
   python manage.py runserver
   ```
   
