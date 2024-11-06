# Generated by Django 4.2.16 on 2024-11-04 02:13

from django.db import migrations, models
import shop.apps.user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_profile_gstin_alter_profile_pan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gstin',
            field=models.CharField(db_index=True, default=None, max_length=15, null=True, validators=[shop.apps.user.models.validate_length(15)], verbose_name='GSTIN Number'),
        ),
    ]