# Generated by Django 3.2.12 on 2022-02-03 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_course', '0003_episode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_course.course')),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app_course.season'),
            preserve_default=False,
        ),
    ]
