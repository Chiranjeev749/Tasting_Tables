# Generated by Django 4.1.7 on 2023-05-15 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='type',
            field=models.CharField(choices=[('veg', 'veg'), ('non-veg', 'non-veg')], default='non-veg', max_length=10, null=True),
        ),
    ]
