# Generated by Django 3.0.6 on 2020-06-02 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='total_fee',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
