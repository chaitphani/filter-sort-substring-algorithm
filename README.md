# filter-sort-substring-algorithm

This project is mostly concentrated on filtering the data which we used to get from DB using ORM. it contains casual CURD operation of REST APIs and test cases as well.


# installation process and setup

1. to setup the local server have to create a virtual environment by using -> python -m venv venv

2. activate the env which created in previous step (venv/scripts/activate.bat)

3. simply have to install the dependencies used for this project with a cmd -> pip install -r requirements.txt (can find all the dependencies within requirements.txt file which has been included in the project dir)

4. after successful installation run the server with cmd -> python manage.py runserver

5. for easy access and testing added user_data.json file which can be uploaded through django admin panel.

6. provided with a import option inside the userdata model it will be easier to import all the data into DB.

# working with test cases.

1. added and configures django-pytest for testing the APIs in this project.

2. setup is done in pytest.ini file which can be found in project dir.

3. to run all the test cases simply run py.test or pytest cmd.
