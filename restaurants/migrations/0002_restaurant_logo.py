# Generated by Django 2.1.5 on 2019-08-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
