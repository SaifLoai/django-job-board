from django.db import models
from django.template.defaultfilters import slugify
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

    slug = models.SlugField(blank=True,null=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        return super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class Apply(models.Model):
    job = models.ForeignKey("Job", related_name="apple_job", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    cv = models.FileField( upload_to='apply/', max_length=100)
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name