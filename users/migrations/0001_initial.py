# Generated by Django 3.0.5 on 2020-10-21 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='none', max_length=60)),
                ('last_name', models.CharField(default='none', max_length=60)),
                ('language', models.CharField(default='none', max_length=60)),
                ('date_of_birth', models.DateField(blank=True, max_length=8, null=True)),
                ('busy', models.BooleanField(default=False)),
                ('can_post', models.BooleanField(default=True)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_client', models.BooleanField(default=False)),
                ('business_name', models.CharField(default='none', max_length=60)),
                ('business_type', models.CharField(default='none', max_length=60)),
                ('description', models.TextField(default='none', max_length=5000)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('image', models.ImageField(default='profile-blank.png', upload_to='profile_pics')),
                ('stripe_user_id', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
