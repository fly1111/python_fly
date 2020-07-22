from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=32)
    price  =models.DecimalField(max_digits=5,decimal_places=2)
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")
    pub_date = models.DateField()
class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail =models.OneToOneField("AuthorDetail",on_delete=models.CASCADE)
class AuthorDetail(models.Model):
    gender_choices = (
            (0,"女"),
            (1,"男"),
            (2,"保密"),)
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()
class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(decimal_places=2,max_digits=9)
class Login(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
