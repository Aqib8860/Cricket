# Generated by Django 3.1.3 on 2021-02-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0005_auto_20210205_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='status',
            field=models.CharField(choices=[('Running', 'Running'), ('Finished', 'Finished'), ('Pending', 'Pending'), ('Canceled', 'Canceled'), ('Upcoming', 'Upcoming')], default='Upcoming', max_length=200, null=True),
        ),
    ]
