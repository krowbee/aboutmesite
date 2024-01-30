from django.db import models

# Create your models here.

class AboutWork(models.Model):
    image = models.CharField(("Картинка"), max_length=50)
    title = models.CharField(("Название"),max_length=50)
    text = models.TextField(("Text"))


class MySkill(models.Model):
    
    image = models.CharField(("Картинка"), max_length=50)
    title = models.CharField(("Название"),max_length=50)
    text = models.TextField(("Text"))