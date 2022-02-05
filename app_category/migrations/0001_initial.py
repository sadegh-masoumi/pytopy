# Generated by Django 3.2.12 on 2022-02-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160, verbose_name='نام')),
                ('slug', models.SlugField(allow_unicode=True, unique=True, verbose_name='نام در url')),
                ('title_page_atc', models.CharField(max_length=100, null=True)),
                ('des_page_atc', models.TextField(null=True)),
                ('title_page_frm', models.CharField(max_length=100, null=True)),
                ('des_page_frm', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
    ]
