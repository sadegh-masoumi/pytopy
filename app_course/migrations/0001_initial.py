# Generated by Django 4.0.1 on 2022-01-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, unique=True, verbose_name='نام در url')),
                ('name', models.CharField(max_length=150, verbose_name='نام')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('main_image', models.FileField(blank=True, null=True, upload_to='course/images/main', verbose_name='عکس اصلی')),
                ('alt_image', models.CharField(blank=True, max_length=100, null=True, verbose_name='alt عکس')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='تخفیف')),
                ('title_page', models.CharField(max_length=160, verbose_name='عنوان صفحه محصول(برای SEO)')),
                ('description_page', models.CharField(max_length=340, verbose_name='توضیحات صفحه محصول(برای SEO)')),
                ('is_active', models.BooleanField(default=True, verbose_name='موجود/ناموجود')),
            ],
        ),
    ]
