# Generated by Django 3.2 on 2022-11-29 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0015_alter_user_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fee',
            field=models.IntegerField(),
        ),
    ]