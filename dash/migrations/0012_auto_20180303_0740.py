# Generated by Django 2.0.2 on 2018-03-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0011_auto_20180302_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Question Number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='our_answer',
            field=models.CharField(default='', max_length=100),
        ),
    ]
