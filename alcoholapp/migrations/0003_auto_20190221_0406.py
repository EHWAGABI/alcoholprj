# Generated by Django 2.1.7 on 2019-02-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alcoholapp', '0002_auto_20190221_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/', upload_to='images/'),
        ),
    ]
