from django.db import models
import os
from uuid import uuid4
# Create your models here.

JOB_TYPE = (
    ('full time','Full time'),
    ('part time','Part time'),
)

def image_upload(instance,filename):
    upload_to = 'jobs/'
    ext = filename.split('.')[-1]

    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

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
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name