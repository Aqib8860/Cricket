# Generated by Django 3.1.3 on 2021-02-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0011_auto_20210205_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_cap',
            field=models.BooleanField(default=False, null=True),
        ),
    ]