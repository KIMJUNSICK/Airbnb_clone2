# Generated by Django 2.2.5 on 2019-11-29 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191129_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='gener',
            new_name='gender',
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]