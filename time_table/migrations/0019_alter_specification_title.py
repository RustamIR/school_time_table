# Generated by Django 3.2.2 on 2021-05-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_table', '0018_alter_teacher_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='title',
            field=models.TextField(max_length=255, verbose_name='Название спецификации'),
        ),
    ]
