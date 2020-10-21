# Generated by Django 3.0.5 on 2020-10-21 04:25

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
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(blank=True, max_length=120)),
                ('active', models.BooleanField(default=True)),
                ('number_of_post', models.IntegerField()),
                ('length', models.IntegerField()),
                ('manager_payment', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('price_paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('paid_for', models.BooleanField(default=False)),
                ('job_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('manager_paid', models.BooleanField(default=False)),
                ('job_complete', models.BooleanField(default=False)),
                ('job_rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('captions', models.BooleanField(default=False)),
                ('search_for_content', models.BooleanField(default=False)),
                ('post_for_you', models.BooleanField(default=False)),
                ('engagement', models.BooleanField(default=False)),
                ('service_description', models.CharField(default='none', max_length=5000)),
                ('manager_randomly_assigned', models.BooleanField(default=True)),
                ('auto_renewal', models.BooleanField(default=False)),
                ('cancelled', models.BooleanField(default=False)),
                ('instagram', models.BooleanField(default=False)),
                ('facebook', models.BooleanField(default=False)),
                ('instagram_username', models.CharField(blank=True, default='none', max_length=100)),
                ('facebook_username', models.CharField(blank=True, default='none', max_length=100)),
                ('job_preparation_completed', models.BooleanField(default=False)),
                ('job_preparation_deadline', models.DateTimeField(blank=True, max_length=8, null=True)),
                ('date_requested', models.DateTimeField(auto_now_add=True, verbose_name='date requested')),
                ('deadline', models.DateTimeField(blank=True, max_length=8, null=True)),
                ('client_job_rating', models.IntegerField(blank=True, default=0)),
                ('job_offers', models.CharField(blank=True, default='none', max_length=5000)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MilestoneFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestoneOne', models.BooleanField(default=False)),
                ('milestoneTwo', models.BooleanField(default=False)),
                ('milestoneThree', models.BooleanField(default=False)),
                ('milestoneFour', models.BooleanField(default=False)),
                ('milestoneFile', models.FileField(upload_to='')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.JobPost')),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestone_number', models.IntegerField(default=0)),
                ('milestone_rating', models.IntegerField(default=0)),
                ('milestone_statement', models.CharField(default='none', max_length=1000)),
                ('milestone_post_goal_completed', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('deadline', models.DateTimeField(blank=True, max_length=8, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.JobPost')),
            ],
        ),
    ]