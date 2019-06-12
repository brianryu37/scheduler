from django.conf import settings
from django.db import models

class Instructor(models.Model):
    identification = models.CharField(max_length = 12)
    rank = models.CharField(max_length = 2)
    name = models.CharField(max_length = 40)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, default = None, blank = True, null = True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length = 20)
    identification = models.CharField(max_length = 12)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, default = None, blank = True, null = True)
    
    def __str__ (self):
        return self.name

class Room(models.Model):
    number = models.CharField(max_length = 6)

    def __str__ (self):
        return self.number

