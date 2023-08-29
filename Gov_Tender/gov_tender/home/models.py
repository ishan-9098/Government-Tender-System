from django.db import models

# Create your models here.

class feedback(models.Model):
    name = models.CharField(max_length=50)
    suggestions = models.CharField(max_length=125)
    rating = models.CharField(max_length=50)

class Company_profile(models.Model):
    C_id = models.CharField(max_length=10)
    C_name = models.CharField(max_length=50)
    C_phone =models.CharField(max_length=15)
    C_add = models.CharField(max_length=122)
    C_email =  models.CharField(max_length=50)
    C_username = models.CharField(max_length = 20)

class tender(models.Model):
    t_id = models.CharField(max_length=10)
    sector_name = models.CharField(max_length=25)
    Time_dur = models.CharField(max_length=25)
    price = models.CharField(max_length=20)
    Start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=10)
    descreption = models.CharField(max_length=100)


class create_progress(models.Model):
    t_Id = models.CharField(max_length=10)
    descreption = models.CharField(max_length=200)

class applications(models.Model):
    tid = models.CharField(max_length=10)
    company_name = models.CharField(max_length=50)
