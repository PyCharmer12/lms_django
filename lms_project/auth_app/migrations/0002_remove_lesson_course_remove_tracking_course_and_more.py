# Generated by Django 4.2.5 on 2023-10-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='course',
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.DeleteModel(
            name='Tracking',
        ),
    ]