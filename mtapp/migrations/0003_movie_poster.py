# Generated by Django 2.0.5 on 2019-07-24 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtapp', '0002_auto_20190720_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
