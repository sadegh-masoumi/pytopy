# Generated by Django 3.2.12 on 2022-02-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_course', '0005_season_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='discount',
            field=models.IntegerField(default=0, verbose_name='درصد تخفیف'),
        ),
    ]