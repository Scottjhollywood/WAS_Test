# Generated by Django 3.2 on 2021-04-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=100)),
                ('body_text', models.CharField(default='body', max_length=250)),
                ('pub_date', models.DateTimeField(default=1089, verbose_name='date published')),
            ],
        ),
    ]
