# Generated by Django 3.2 on 2022-11-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_instrument_inst_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=20)),
            ],
        ),
    ]