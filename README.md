# Django
start with Django 
# install 
# setup virtual enviorment for project
>## pip install virtualenvwrapper-win
> why? because every project have diff setting of django so we create separate env. we 
> cann't create env than same setting for all django project
# create enviroment
>## mkvirtualenv Project_name
# install Django
>## pip install django
# run if work env is not run eg.(test)D:\\.....
>## workon test(work env name)
# make project dir
> mkdir project_folder_name
>> cd project_folder_name
# start project
>## django-admin startproject
# Access server
>## python manage.py runserver
# start app
>## python manage.py startapp (app_name)
# add template
> create a folder with any name(ex. templates)
> this folder contain all view(ex.- html file)
> before creating we need add some line to settings.py file
>##   Templates = [ 
>      { 'DIRS' : [os.path.join(BASE_DIR,'folder_name(ex. template)') 
>       }
>      ]  
>>add these line in setting file and TEMPLATES* field 

# add jinja code
>#### {% block content %} 
>#### {% endblock %}    
>> for dyanamic content 

# sending data using POST 
> for these use {% csrf_token %}
