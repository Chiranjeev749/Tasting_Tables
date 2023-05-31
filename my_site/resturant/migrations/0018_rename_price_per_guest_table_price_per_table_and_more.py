# Generated by Django 4.1.7 on 2023-05-21 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0017_remove_table_no_of_guests_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='price_per_guest',
            new_name='price_per_table',
        ),
        migrations.AlterField(
            model_name='table',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturant.restaurant'),
        ),
    ]
