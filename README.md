# backend-emora

# How to deploy app django to heroku with addons postgresql




1- Install dependence django in local

	=> pip install django django-cors-header  django-heroku gunicorn psycopg2 dj-database-url

2- Touch file runtime.txt in same directory manage.py

	- add python-<your_version_python>
	
	=> Python version available for runtime for heroku stack is: 
	
	
	- default stack for python3  is heroku-20
	
	
	-Supported runtimes
		-python-3.9.6 on all supported stacks : for heroku-20, heroku-18
		-python-3.8.11 on all supported stacks: for heroku-20, heroku-18
		-python-3.7.11 on all supported stacks: for heroku-18
		-python-3.6.14 on all supported stacks:


	- for example
	- in runtime.txt
		python-3.8.11
3- Create file requirements.txt for yoour app:
	
  Easy command for create requeriments.txt
  - 
	 => python -m pip freeze>requirements.txt
   
	And you have been create file requirements.txt with all module list 
  
4- Create Procfile:
	and add this: 
  
  - web: gunicorn <your_app_name>.wsgi:application --log-file -

5- Settings files settings.py
	- import this after import os: 
		import django_heroku
		import dj_database_url

	- add replace STATIC_URL = '/static/'

		to

		STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
		STATIC_URL = '/static/'
		STATICFILES_DIRS =(os.path.join(BASE_DIR, 'static'), )
		django_heroku.settings(locals())

	- and create directory folder "static" in same directory manage.py

6- Git and heroku cli
	 
   
  - Initial git and add in repo
  
    => git init

    => git add .

 
	- create account heroku and login in cli
  
    => heroku login
    
    =>heroku create <your_app_name>
     
=> git push heroku master


7- Heroku postgres
	- Open your heroku dashbord and click you app
		-and click heroku-postgresql
		-and got to settings
		-and Database credentials/View Credentials
		-and Change you config DATABASE in settings.py

	DATABASES = {
   	 'default': {
        		'ENGINE': 'django.db.backends.postgresql_psycopg2',

       		 'NAME': 'your_database_name',

      		  'USER': 'your_database_users',

        		'PASSWORD': 'your_database_password',

        		'HOST': 'your_host_name',

       		 'PORT': 'your_port',
   		 }
	}


8- and git add / commit/ push heroku master

9- You app is deployeing in Heroku, you can visit 







