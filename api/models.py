from django.db import models

# Create your models here.

# Company model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), ('Non IT', 'Non IT'), ('Service', 'Service')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Employee model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(('Manager', 'Manager'), ('Product Owner', 'Product Owner'), ('Tester', 'Tester')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)


class Manager(models.Model):
    
    name = models.CharField(max_length=100)
    aim = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
