# Django API

Quick demo for creating an API with Django rest_framework and coreapi. This allows for easy connection with local and cloud databases, as well as creating the right documentation for the endpoints

Needs to implement the front-end part

&nbsp;

/docs will take you here
![API docs](https://github.com/DanielGit28/DjangoAPI/assets/68488204/991386b0-e7e8-49c5-b2d6-631ce6e2ed47)

/api/v1 will take you to the default page where all entities will be listed
![api default page](https://github.com/DanielGit28/DjangoAPI/assets/68488204/74308897-4d7a-43cd-8546-42175f1f76b2)

/api/v1/{modelName} will take you to the info page of that object or model. It will also list the first saved objects and also has a form to manually add an object from that model type
![Model page](https://github.com/DanielGit28/DjangoAPI/assets/68488204/382f4376-957f-4281-94d4-a7f68090d9b8)
and adding a number after the {modelName} will fetch you the object with that id: /api/v1/{modelName}/2

&nbsp;



## 🚀 Quick Start


When you're ready to start the project, run the following commands:

This runs the server
```sh
python manage.py runserver    
```

When you need to update the models and views, you run these commands:
```sh
python manage.py makemigrations 
```
```sh
python manage.py migrate     
```
```sh
python manage.py createsuperuser 
```
And with that, Django will make sure to update the necessary things in the db connection and schema

If you need new dependencies (libraries), to install them you run this: 
```sh
pip install djangorestframework 
```
And change 'djangorestframework' for the required name






 
