# Generated by Django 5.0.2 on 2024-03-06 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomcitydata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
