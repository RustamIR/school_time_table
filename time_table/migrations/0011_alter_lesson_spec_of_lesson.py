# Generated by Django 3.2.2 on 2021-05-13 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_table', '0010_auto_20210513_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='spec_of_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='time_table.specification'),
        ),
    ]
