# Generated by Django 3.2.6 on 2021-09-01 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['create']},
        ),
    ]