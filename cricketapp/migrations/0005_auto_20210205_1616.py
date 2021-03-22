# Generated by Django 3.1.3 on 2021-02-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0004_auto_20210205_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='matchDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='status',
            field=models.CharField(choices=[('Running', 'Running'), ('Finished', 'Finished'), ('Pending', 'Pending'), ('Canceled', 'Canceled'), ('Upcoming', 'Upcoming')], default='Pending', max_length=200, null=True),
        ),
    ]
