# Generated by Django 3.2.2 on 2021-06-10 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_table', '0023_auto_20210610_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='lessons',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_lessons', to='time_table.lesson', verbose_name='Уроки учителя'),
            preserve_default=False,
        ),
    ]
