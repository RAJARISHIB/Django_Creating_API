# Django_Creating_API
An overview of the projet.
The project focues on creating an API using Django and restframework, I created an app which contains "Course_name" and "Course_id" and we manipulate and use the API using postman
Step by step process:
Step1:
  Install django
  startproject projectname
  startapp appname
  create viritual enviroinment
  **** Make sure to add the appanme in the settings.py present in project ***
  *** also remember to add the restframework in the settings.py ***
  create a urls.py in the app
  create model class
  create serializers
  add the serializers in the view
  create router and add the viewclas to the router in urls.py
  in the admin register the viewclass
Views - it tells what data to be shown to the user it gets it data from seralizers ( which is used to convert the json to python format )
Serializers - it gets its input from the models which provides the input
Models - models is where you set which information to get
make sure to register the model  view in admin
