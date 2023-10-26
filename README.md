# Django Video Series - Day 1: Getting Started

Welcome to Day 1 of our Django video series! In this episode, we will guide you through the essential steps to set up your Django project. By the end of this tutorial, you'll have a Django project up and running, complete with a custom app, and you'll understand the basic workflow.

## Prerequisites

Before you begin, make sure you have the following installed on your system:
- Python 3.x
- Virtualenv (for creating a virtual environment)

## Step 1: Setting Up a Virtual Environment

First, let's create a virtual environment for our Django project. Open your terminal or command prompt and run the following commands:

```bash
# Create a new directory for your project
mkdir myproject

# Navigate into the project directory
cd myproject

# Create a virtual environment (replace 'env' with your preferred name)
python -m venv django_env

# Activate the virtual environment
# On Windows
django_env\Scripts\activate
# On macOS and Linux
source django_env/bin/activate
```

## Step 2: Installing Django

With your virtual environment activated, you can now install Django. Run the following command:

```bash
# install django
pip install django
```

## Step 3: Creating a Django Project

Let's create a new Django project. Replace 'myproject' with your preferred project name.

```bash
# start project
django-admin startproject mywebsite
```

## Step 4: Creating a Django App

Now, let's create a Django app within our project. Replace 'myapp' with your preferred app name.

```bash
# start app
python manage.py startapp myapp
```

## Step 5: Running Migrations

Django uses migrations to manage the database schema. Run the following commands to apply initial migrations:

```bash
# start app
python manage.py makemigrations
python manage.py migrate
```

## Step 6: Creating a Superuser

You can create a superuser account to access the Django admin panel and manage your app's data.

```bash
# create superuser
python manage.py createsuperuser
```

## Step 7: Starting the Development Server

Finally, let's start the Django development server:

```bash
# run server
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your web browser to see your Django app in action. Access the admin panel at http://127.0.0.1:8000/admin/ and log in using the superuser credentials.
