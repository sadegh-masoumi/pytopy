# Generated by Django 3.2.12 on 2022-02-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_course', '0004_auto_20220203_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
