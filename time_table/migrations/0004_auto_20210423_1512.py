# Generated by Django 2.2.6 on 2021-04-23 15:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_table', '0003_auto_20210411_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='classroom',
            name='count_seats',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество мест в классе'),
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='lessons',
        ),
        migrations.CreateModel(
            name='LessonsClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_name', to='time_table.Class')),
                ('lessons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='les', to='time_table.Lessons')),
            ],
        ),
        migrations.AddField(
            model_name='timetable',
            name='lessons',
            field=models.ManyToManyField(related_name='lessons_title', to='time_table.LessonsClass', verbose_name='Название урока'),
        ),
    ]