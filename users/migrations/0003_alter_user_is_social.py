# Generated by Django 3.2.2 on 2021-05-20 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_social',
            field=models.CharField(max_length=500),
        ),
    ]
