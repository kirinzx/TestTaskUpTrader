# Generated by Django 4.2.6 on 2023-12-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treeMenu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]