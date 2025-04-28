# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

admin.py


from django.contrib import admin

from .models import Movies,MoviesAdmin

admin.site.register(Movies,MoviesAdmin)


models.py

from django.db import models

from django.contrib import admin

class Movies(models.Model):

    userid=models.IntegerField(primary_key=True)
    
    username=models.CharField(max_length=30)
    
    mobileno=models.IntegerField()
    
    mailid=models.EmailField()
    
    moviename=models.CharField(max_length=50)
    
    noofseats=models.IntegerField()
    
    date=models.DateField()

class MoviesAdmin(admin.ModelAdmin):

    list_display=('username','moviename','noofseats','mailid')



## OUTPUT

Include the screenshot of your admin page.![Screenshot (296)](https://github.com/user-attachments/assets/61c4372d-2609-47bf-9f51-be36f421e7f7)



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
