# Generated by Django 2.0.2 on 2018-02-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='time_done',
        ),
        migrations.AddField(
            model_name='question',
            name='duration_factor',
            field=models.IntegerField(choices=[(60, 'min'), (1, 'sec')], default=60),
        ),
        migrations.AddField(
            model_name='question',
            name='duration_value',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
