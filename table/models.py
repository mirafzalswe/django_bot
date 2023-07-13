from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    telegram_id = models.BigIntegerField()
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    telegram_id = models.BigIntegerField()
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


