from django.db import models
from django.db.models import Model


# Create your models here.


class Teacher(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Photo = models.ImageField(upload_to='image/', blank=False)
    Date_of_Birth = models.DateField()
    Gender = models.CharField(max_length=200)
    Address = models.TextField(max_length=200)
    State = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    PhoneNumber = models.IntegerField()
    Qualification = models.CharField(max_length=200)
    Date_of_joining = models.DateField()
    Subject = models.CharField(max_length=200)
    Class_in_charge = models.CharField(max_length=200)
    UserName = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)


class Student(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Photo = models.ImageField(upload_to='image/', blank=False,)
    Date_of_Birth = models.DateField(default=False)
    Gender = models.CharField(max_length=100, default=False)
    Address = models.TextField(max_length=200)
    State = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Guardian_Name = models.CharField(max_length=200)
    PhoneNumber1 = models.IntegerField()
    PhoneNumber2 = models.IntegerField()
    Class = models.CharField(max_length=200)
    Academic_Year = models.IntegerField()
    Area_of_Interest = models.CharField(max_length=200)
    UserName = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Status = models.CharField(max_length=100)


class Login(models.Model):
    Type = models.CharField(max_length=100)
    UserName = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)


class Note(models.Model):
    Class = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Chapter = models.CharField(max_length=200)
    Note = models.FileField(upload_to='files/')


class Assignment(models.Model):
    Class = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Assignment = models.FileField(upload_to='files/')


class TimeTable(models.Model):
    Class = models.CharField(max_length=200)
    TimeTable = models.FileField(upload_to='files/')


class Attendance(models.Model):
    Class = models.CharField(max_length=200)
    Month = models.CharField(max_length=100, default=False)
    Attendance = models.FileField(upload_to='files/')

