# Generated by Django 4.1.7 on 2023-05-16 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0006_rename_city_profile_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='PhoneNo',
            new_name='phoneNo',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Pin',
            new_name='pin',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='State',
            new_name='state',
        ),
    ]
