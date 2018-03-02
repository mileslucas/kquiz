# Generated by Django 2.0.2 on 2018-03-02 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dash', '0006_auto_20180302_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Event')),
                ('location', models.CharField(max_length=200, verbose_name='Location')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('time', models.DateTimeField(verbose_name='Time')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('respondents', models.ManyToManyField(default=None, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]