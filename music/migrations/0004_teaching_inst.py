# Generated by Django 3.2 on 2022-11-27 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='teaching_inst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teaching_inst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.instrument')),
            ],
        ),
    ]