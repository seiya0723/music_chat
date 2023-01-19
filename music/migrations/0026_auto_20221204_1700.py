# Generated by Django 3.2 on 2022-12-04 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0025_auto_20221203_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrument',
            name='user',
        ),
        migrations.AddField(
            model_name='teacher',
            name='user_id',
            field=models.ForeignKey(default='9999', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='email'),
        ),
    ]