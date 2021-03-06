# Generated by Django 4.0.3 on 2022-04-08 08:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NewsPortal', '0002_alter_comment_date_of_creation_alter_comment_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 8, 11, 23, 20, 202579)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 8, 11, 23, 20, 200579)),
        ),
    ]
