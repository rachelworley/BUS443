from django.db import models

# Create your models here.
class Studentdetails(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    major = models.CharField(max_length=256)
    year = models.CharField(max_length=256)
    gpa = models.DecimalField(decimal_places=2, max_digits=5)

class Courseinfo(models.Model):
    courseid = models.IntegerField(primary_key=True)
    coursetitle = models.CharField(max_length=256)
    coursename = models.CharField(max_length=256)
    courseselectioncode = models.IntegerField()
    coursedepartment = models.CharField(max_length=256, default='SOME STRING')
    instructorname = models.CharField(max_length=256, default='SOME STRING')

class Registrar(models.Model):
    studentid= models.IntegerField()
    courseid = models.IntegerField()
    coursename = models.CharField(max_length=256)
    instructorname = models.CharField(max_length=256, default='SOME STRING')