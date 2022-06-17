# Generated by Django 3.2 on 2022-06-17 11:35

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhood', '0004_post_posttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('start_day', models.CharField(max_length=50)),
                ('end_day', models.CharField(max_length=50)),
                ('open_time', models.CharField(max_length=50)),
                ('close_time', models.CharField(max_length=50)),
                ('bs_image', cloudinary.models.CloudinaryField(default='image/upload/v1627341811/company_default_qb4ili.png', max_length=255, verbose_name='images')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhood.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhood.profile')),
            ],
        ),
    ]