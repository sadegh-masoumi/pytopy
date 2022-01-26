from django.views.generic import TemplateView

# from ptp_article.models import Article
# from ptp_userInforamtion.models import UserInformation


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # article = Article.articles.all().order_by('-id')
        # user_information = UserInformation.objects.filter(user_id__in=article.values_list('user_id', flat=True))
        #
        # context['articles'] = article
        # context['userInformation'] = user_information

        return context
