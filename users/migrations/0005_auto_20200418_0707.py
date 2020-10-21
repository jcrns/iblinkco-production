# Generated by Django 3.0.5 on 2020-04-18 07:07

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200418_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='none', max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='profile-blank.png', force_format=None, keep_meta=True, quality=0, size=[300, 300], upload_to='profile_pics'),
        ),
    ]