from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
   
    def __str__(self):
        return self.username
    

class School(models.Model):
    school_name = models.CharField(max_length=255)
    y = models.FloatField()
    x = models.FloatField()
    type_of_school = models.CharField(max_length=255)
    study_period = models.CharField(max_length=255)
    educational_level = models.CharField(max_length=255)
    number_of_classes = models.JSONField()
    computer_lab = models.IntegerField()
    science_lab = models.IntegerField()
    physics_lab = models.IntegerField()
    chemistry_lab = models.IntegerField()
    biology_lab = models.IntegerField()
    administrative_rooms = models.IntegerField()
    stage = models.CharField(max_length=255)
    mosque = models.CharField(max_length=255)
    ambulance_room = models.CharField(max_length=255)
    specialist_room = models.CharField(max_length=255)
    library = models.CharField(max_length=255)
    canteen = models.CharField(max_length=255)
    guard_room = models.CharField(max_length=255)
    playgrounds = models.CharField(max_length=255)
    bathrooms = models.IntegerField()
    academic_level = models.CharField(max_length=255)
    num_libyan_males = models.IntegerField()
    num_libyan_females = models.IntegerField()
    num_foreign_males = models.IntegerField()
    num_foreign_females = models.IntegerField()
    num_males_special_categories = models.IntegerField()
    num_females_special_categories = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.school_name

class AcademicLevel(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='academic_levels')
    academic_level = models.CharField(max_length=255)
    num_libyan_males = models.IntegerField()
    num_libyan_females = models.IntegerField()
    num_foreign_males = models.IntegerField()
    num_foreign_females = models.IntegerField()
    num_males_special_categories = models.IntegerField()
    num_females_special_categories = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.id