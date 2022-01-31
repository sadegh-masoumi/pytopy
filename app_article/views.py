from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect

from .models import ArticleComments
from app_user.models import Follow
from app_user.models import User
from .models import Article
from app_category.models import Category
from .forms import ArticleCommentForm


def view_articles(request):
    articles: Article = Article.articles.all().order_by('-id')
    category = Category.objects.all()
    lastArticle = Article.articles.order_by('-date')

    userInformation = User.objects.filter(pk__in=articles.values_list('user_id', flat=True))
    # -------------------page paginator -------------

    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'articles': page_obj,
        'category': category,
        'lastArticle': lastArticle,
        'paginator': paginator,
        "userInformation": userInformation
    }
    return render(request, 'articles.html', context)


def view_article_category(request, slug):
    articles = Article.articles.filter(category__slug__in=[slug])
    category = Category.objects.all()
    category_selected = Category.objects.filter(slug=slug).first()

    userInformation = User.objects.filter(user_id__in=articles.values_list('user_id', flat=True))
    # -------------------page paginator -------------

    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'article': page_obj,
        'category': category,
        'category_selected': category_selected,
        "userInformation": userInformation
    }
    return render(request, 'articles_category.html', context)


def view_article_detail(request, article_id, slug):
    article = Article.articles.filter(id=article_id).first()
    if article is None:
        raise Http404('مقاله مورد نظر یافت نشد')

    articleComments = ArticleComments.objects.filter(article=article, is_active=True)

    commentForm = ArticleCommentForm(request.POST or None)
    userInformation = User.objects.filter(user=article.user).first()
    context = {
        'article': article,
        'comment': False,
        'commentForm': commentForm,
        'follow_alert': False,
        'login_required': False,
        'follow': None,
        'userInformation': userInformation,

        'articleComments': articleComments
    }

    if commentForm.is_valid():
        name = commentForm.cleaned_data.get('name')
        email = commentForm.cleaned_data.get('email')
        description = commentForm.cleaned_data.get('description')
        try:
            assert name is not None or email is not None or description is not None
        except:
            raise Http404('لطفا فرم را کامل پر کنید')
        ArticleComments.objects.create(article=article, name=name, email=email, description=description)
        context['comment'] = True

    if request.user.is_authenticated:
        context['follow'] = Follow.objects.filter(follower=request.user).first()

    if request.GET.get('unfollow') is not None:
        user = request.user
        if user is not None:
            unfollow = request.GET.get('unfollow')
            if context['follow'] is not None:
                Follow.objects.filter(follower_id=unfollow, following_id=user.id).delete()
                context['unfollow_alert'] = True
                context['follow'] = None
            else:
                return redirect(f'/article-detail/{article.id}/{article.slug}')

    if request.GET.get('follow') is not None:
        user = request.user
        if request.user.is_authenticated:
            follow = request.GET.get('follow')
            if context['follow'] is None:
                context['follow'] = Follow.objects.create(follower_id=follow, following_id=user.id)
                context['follow_alert'] = True
            else:
                return redirect(f'/article-detail/{article.id}/{article.slug}')
        else:
            context['login_required'] = True

    return render(request, 'article_detail.html', context)
