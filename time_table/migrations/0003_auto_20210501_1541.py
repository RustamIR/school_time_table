# Generated by Django 3.2 on 2021-05-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_table', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['title'], 'verbose_name': 'Класс', 'verbose_name_plural': 'Классы'},
        ),
        migrations.AlterField(
            model_name='class',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название класса'),
        ),
    ]
