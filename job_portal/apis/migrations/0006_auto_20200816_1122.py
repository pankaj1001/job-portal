# Generated by Django 3.1 on 2020-08-16 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_auto_20200816_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='job_poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
