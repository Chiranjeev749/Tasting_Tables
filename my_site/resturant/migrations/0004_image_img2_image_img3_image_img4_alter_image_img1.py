# Generated by Django 4.1.7 on 2023-05-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img2',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='img3',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='img4',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='img1',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]