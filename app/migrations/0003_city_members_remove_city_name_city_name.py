# Generated by Django 4.1 on 2022-08-31 17:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_remove_city_name_city_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='city',
            name='name',
        ),
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Город'),
        ),
    ]