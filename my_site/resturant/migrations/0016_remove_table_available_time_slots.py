# Generated by Django 4.1.7 on 2023-05-21 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0015_alter_reservation_table_alter_table_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='available_time_slots',
        ),
    ]
