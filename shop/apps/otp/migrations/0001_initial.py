# Generated by Django 4.2.15 on 2024-09-04 09:29

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
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_secret', models.CharField(max_length=16, verbose_name='OTP Secret')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Verified')),
                ('to_email', models.BooleanField(default=False, verbose_name='To Email')),
                ('to_phone', models.BooleanField(default=False, verbose_name='To Phone')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('changed_date', models.DateTimeField(auto_now=True, verbose_name='Updated On')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]