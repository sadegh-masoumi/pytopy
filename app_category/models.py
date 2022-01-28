from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=160, verbose_name='نام')
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name='نام در url')

    # page title and description for Articles category
    title_page_atc = models.CharField(max_length=100, null=True)
    des_page_atc = models.TextField(null=True)

    # page title and description for Forum category
    title_page_frm = models.CharField(max_length=100, null=True)
    des_page_frm = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
