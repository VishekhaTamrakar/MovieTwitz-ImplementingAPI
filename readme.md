# MovieTwist

This application is developed as a part of class project in ISQA 8380 Assignment 4.

Heroku - 

## Prerequisites

1. Python installed in your system

## Steps to run

1. Clone this repository in your local

2. Create a virtual environment in the parent directory to setup the runtime environment

   `python -m venv myvenv`

   On Mac this would be

   `python3 -m virtualenv myvenv`

   Make sure that you don't have **myvenv** in the same directory as the project and git is not tracking it. An ideal folder tree would look like -

   ```
   movietwizt
   |-- mtzt
      |-- mtapp
      |-- mtzt
      |-- db.sqlite3
   |-- myvenv
   ```

3. Activate the virtual environment by going to `myvenv/Scripts/` and running the script `activate`

4. Install Django

   `pip install django==2.0.5`
   'pip install django -paypal'
   'pip install pillow'
   'pip install django-crispy-forms'

5. Run the below command to install the applications and dependencies

   `pip install -r requirements.txt`

6. Migrate to create the tables and create a super user

   `python manage.py migrate`

   `python manage.py createsuperuser`

7. Add local settings to `mtzt/local_settings.py`, i.e. in the same folder as `settings.py`

8. In local_settings.py add the below code

   ```python
   import os
   
   BASE_DIR = os.path.dirname(os.path.dirname(__file__))
   
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       }
   }
   
   DEBUG = True
   ```

9. Run the local server by going to [http://127.0.0.1:8000](http://127.0.0.1:8000/)



## Collaborators

1. Nainsi Kamthan (nkamthan@unomaha.edu)
2. Harwinder Kaur (hharwinderkaur@unomaha.edu)
3. Vishekha Tamrakar (vtamrakar@unomaha.edu)
4. Kumar Vikash (vikashkumar@unomaha.edu)
