# Generated by Django 3.0.5 on 2020-05-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='cover_profile_img'),
        ),
    ]
