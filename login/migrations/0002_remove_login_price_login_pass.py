# Generated by Django 4.0.5 on 2022-06-18 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='price',
        ),
        migrations.AddField(
            model_name='login',
            name='Pass',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
