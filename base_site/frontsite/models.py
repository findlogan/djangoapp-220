from django.db import models

class Merchandise(models.Model):
    name = models.CharField(max_length=100)
    imgURL = models.ImageField(upload_to='pics')
    modalVal = models.CharField(max_length=20)
    desc = models.TextField()

class Sandwhiches(models.Model):
    name = models.CharField(max_length=100)
    imgURL = models.ImageField(upload_to='pics')
    modalVal = models.CharField(max_length=20)
    desc = models.TextField()

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    imgURL = models.ImageField(upload_to='pics')
    modalVal = models.CharField(max_length=20)
    desc = models.TextField()

class Beer(models.Model):
    name = models.CharField(max_length=100)
    imgURL = models.ImageField(upload_to='pics')
    modalVal = models.CharField(max_length=20)
    desc = models.TextField()