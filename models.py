from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    Post_Name =models.CharField(max_length=225)
    Status = models.CharField(max_length=225)
    Field = models.CharField(max_length=225)
    Contant = models.TextField()
    User_ID = models.IntegerField()
    def __str__(self):
        return  "{}".format(self.Contant)    
class Vacancy(models.Model):
    VacancyName = models.CharField(max_length=225)
    Title = models.CharField(max_length=225)
    Requirement = models.TextField()
    Type = models.CharField(max_length=225)
    CompanyID = models.IntegerField()
    def __str__(self):
        return "{}".format(self.Requirement)

class Follow(models.Model):
    User_ID = models.IntegerField()
    FollowsID = models.IntegerField()
    FollowerID = models.IntegerField()