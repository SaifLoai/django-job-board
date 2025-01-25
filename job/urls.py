from django.urls import path , include
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list,name='jobHome'),
    path('add',views.add_job,name='addJob'),
    path('<str:slug>', views.job_detail , name='job_detail'),
]