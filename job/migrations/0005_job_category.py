# Generated by Django 5.1.5 on 2025-01-18 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.category'),
        ),
    ]
