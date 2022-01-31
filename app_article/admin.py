from django.contrib import admin
from .models import Article, Like, ArticleImages, ArticleVideo, ArticleComments

admin.site.register(Article)
admin.site.register(Like)
admin.site.register(ArticleImages)
admin.site.register(ArticleVideo)
admin.site.register(ArticleComments)
