# Generated by Django 4.1.7 on 2023-05-20 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0008_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='Capacity',
            new_name='CapacityPerTable',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='pricePerGuest',
        ),
        migrations.RemoveField(
            model_name='table',
            name='available_time_slots',
        ),
        migrations.AddField(
            model_name='profile',
            name='time_start_of_user',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='table',
            name='name_of_table',
            field=models.CharField(default='standard', max_length=30),
        ),
        migrations.AddField(
            model_name='table',
            name='no_of_guests',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='table',
            name='pricePerGuest',
            field=models.IntegerField(default=100, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='img1',
            field=models.ImageField(default='', upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='table',
            name='resturant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturant.restaurant'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(blank=True, default='', null=True, upload_to='menu/')),
                ('resturant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturant.restaurant')),
            ],
        ),
    ]