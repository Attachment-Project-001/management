# Django School Management

This app is to be used by a school administrator to perfom the following:
    - create and manage students, results and members of staff
    - manage finance record by creating and maintaning invoices and tracking fee payment
    - manage the school data in terms of sessions, terms, Subjects and Classes

Currently it is solely meant for only the school administrator

## Demo
To be created soon

## Usage 
It is recommended to run this projects in a virtual environment(This was developed in a conda environment). Once set up clone this repository.

```bash
git clone <repository link>
```

Change directory to project directory

```
cd school
```

Run project

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver # default http://127.0.0.1:8000
```

#### Admin Login
Migration creates a super user with credentials
    - username: admin123
    - password: admin123

### Development environments
Django version 3.2.5
python version 3.9.6