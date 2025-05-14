from django.db import models
from django.contrib import admin 
class Employee (models.Model):
    eid=models.Charfield(max_length=20,help_text="Employee ID")
    name=models.Charfield(max_length=100)
    Salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    
    class EmployeeAdmin(admin.ModelAdmin):
        list_display=('eid','name','Salary','age','email')