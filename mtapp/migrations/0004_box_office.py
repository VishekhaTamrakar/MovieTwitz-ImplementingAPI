# Generated by Django 2.0.5 on 2019-08-03 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtapp', '0003_movie_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box_Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=10)),
                ('movie_name', models.CharField(max_length=50)),
                ('collection', models.DecimalField(decimal_places=2, max_digits=15)),
                ('rank', models.IntegerField()),
                ('poster', models.CharField(max_length=500, null=True)),
                ('refreshed_date', models.DateField()),
            ],
        ),
    ]