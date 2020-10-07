PYTHON VERSION : 3.7.9 Win64
Django Version: 3.1.2

How to run project:

1) Run these commands: 
	py -m pip install -r requirements.txt
	py manage.py collectstatic
	py manage.py makemigrations
	py manage.py migrate
	py manage.py createsuperuser
	py manage.py runserver

2) Important!! :: Login from admin console and create two Groups 'vendor' and 'bidder'

3) Create Vendor and bidder users from index page.
4) Login with created credentials

Note:
migrations,collectstatic and superusercreation is already done here
just run :
	py -m pip install -r requirements.txt
	py manage.py runserver
and go to 127.0.0.1:8000/ from browser to test out app.

Already created test accounts:

ACCOUNT TYPE	USERNAME	PASSWORD
ADMIN		admin		1234
VENDOR		TEST@VENDOR	TEST@VENDOR
BIDDER		TEST@BIDDER	TEST@BIDDER