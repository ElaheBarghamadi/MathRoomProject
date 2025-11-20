from django.db import models

# Create your models here.
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    GRADE_CHOICES = [
        ('7', 'پایه هفتم'),
        ('8', 'پایه هشتم'),
        ('9', 'پایه نهم'),
    ]

    CLASS_CHOICES = [
        ('701', '۷۰۱'), ('702', '۷۰۲'),
        ('801', '۸۰۱'), ('802', '۸۰۲'),
        ('901', '۹۰۱'), ('902', '۹۰۲'),
    ]

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    classroom = models.CharField(max_length=3, choices=CLASS_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.classroom})"

    class Meta:
        unique_together = ('first_name', 'last_name', 'grade', 'classroom')
