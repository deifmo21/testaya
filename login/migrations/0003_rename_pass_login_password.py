# Generated by Django 4.0.5 on 2022-06-18 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_login_price_login_pass'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='Pass',
            new_name='password',
        ),
    ]
