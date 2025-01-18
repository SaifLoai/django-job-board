from django.db import models

# Create your models here.

JOB_TYPE = (
    ('full time','Full time'),
    ('part time','Part time'),
)

class Job (models.Model): #table for db
    title = models.CharField(max_length=120) #column
    #location
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,null=True) #one to many

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name