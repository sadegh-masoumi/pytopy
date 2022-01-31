from app_user.models import User
from django.db import models
from django.db.models import Q

from app_category.models import Category


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(is_active=True)

    def search(self, query):
        lookup = (
                Q(txt_filter__icontains=query) |
                Q(title__icontains=query) |
                Q(title_page__icontains=query) |
                Q(description_page__icontains=query)
        )
        return self.get_queryset().filter(lookup, is_active=True).distinct()

    def search_by_category(self, query):
        lookup = (
            Q(category__slug__icontains=query)

        )
        return self.get_queryset().filter(lookup, is_active=True).distinct()


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name='دسته بندی')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='سازنده')

    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, verbose_name='نام در url')

    title = models.TextField()

    title_page = models.TextField()
    description_page = models.TextField()

    body = models.TextField()
    txt_filter = models.TextField()

    date = models.DateField(auto_now_add=True, verbose_name='تاریخ')
    is_active = models.BooleanField(default=True)

    cover = models.ImageField(upload_to='Articles/MainImage', null=True, blank=True, default='/Articles/MainImage')
    alt_cover = models.CharField(max_length=100, null=True, verbose_name='alt تصویر')

    prv_article = models.ForeignKey('Article', related_name='prvPost', on_delete=models.RESTRICT,
                                    verbose_name='پست قبلی', null=True, blank=True)
    next_article = models.ForeignKey('Article', related_name='nextPost', on_delete=models.RESTRICT,
                                     verbose_name='پست بعذی', null=True, blank=True)
    articles = ArticleManager()

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    article = models.OneToOneField(Article, on_delete=models.RESTRICT, verbose_name='مقاله')

    def __str__(self):
        return f"{self.user.username} : {self.article.title}"


class ArticleImages(models.Model):
    image = models.ImageField(upload_to='article-image/')


class ArticleVideo(models.Model):
    video = models.FileField(upload_to='article-video/')


class ArticleComments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.RESTRICT, null=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=80)
    description = models.TextField()
    replay = models.ForeignKey('ArticleComments', on_delete=models.CASCADE, verbose_name='ریپلای', blank=True,
                               null=True)
    is_active = models.BooleanField(default=False, verbose_name='نمایش/عدم نمایش')

    def __str__(self):
        return f'{self.name}:{self.email}'
