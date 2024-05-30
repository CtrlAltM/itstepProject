from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Lecture(models.Model):
    name = models.CharField(max_length=50)
    theme = models.CharField(max_length=250)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Member(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    assigned = models.ForeignKey(Member, on_delete=models.CASCADE)
    due = models.DateField()

class Note(models.Model):
    contact = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    note = models.CharField(max_length=5000)