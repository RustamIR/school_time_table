# Generated by Django 2.2.6 on 2021-04-11 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('time_table', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='teachers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_people', to=settings.AUTH_USER_MODEL, verbose_name='Ученики'),
        ),
    ]