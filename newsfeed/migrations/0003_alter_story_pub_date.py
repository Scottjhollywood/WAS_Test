# Generated by Django 3.2 on 2021-04-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0002_alter_story_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
