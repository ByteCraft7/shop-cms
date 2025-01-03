# Generated by Django 4.2.16 on 2024-11-04 08:11

from django.db import migrations, models
import localflavor.in_.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_profile_gstin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pan',
            field=localflavor.in_.models.INPANCardNumberField(db_index=True, default=None, max_length=10, null=True, verbose_name='PAN Number'),
        ),
        migrations.AddConstraint(
            model_name='profile',
            constraint=models.UniqueConstraint(condition=models.Q(models.Q(('pan', ''), _negated=True), ('pan__isnull', False)), fields=('pan',), name='unique_pan_inprofile_ifnotnull'),
        ),
    ]
