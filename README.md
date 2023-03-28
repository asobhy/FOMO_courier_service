# Courier-First
Courier First Delivery System is Web app , Developed using Python Django. 
CFS is develop by alaadin.sobhy@gmail.com

steps to make it working

1. Install python 
2. Install Dajngo  (pip install django)
3. Go to cfs folder
4. runcommand python manage.py runserver
   if Errors : pillow like library then install it.
	and try with step 4.

Admin    :  admin@cfs.com
password :  admin
phone no : 9999222062

Delivery Boy 	: deliveryboy@cfs.com
password 	:  #elloW0rld
phone no	: 9811234599

User	  : alaadin@cfs.com	
password  : #elloW0rld
phone no  : 9810187019

URLS
 admin_page  : http://127.0.0.1:8000/admin/

login url 
  user and delivery agent have to login form same page. 

------------------------------------------------------------

if db.sqlite3 file not avialbel in cfs folder or admin not working.

1. delete db.sqlite3
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py createsuperuser
    you can create new admin form here!
5. python manage.py runserver

