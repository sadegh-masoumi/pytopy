import mimetypes

from core.settings.base import BASE_DIR, DOWNLOAD_API, DEBUG

from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, Http404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse

from app_order.models import Enroll
from .models import Season, Episode, UserDownloadEpisode, Course, CourseComment
from .forms import CourseCommentsForm


class Courses(ListView):
    template_name = 'all_course.html'
    model = Course


def view_single_course(request, pk, **kwargs):
    course = get_object_or_404(Course, id=pk)
    season = Season.objects.filter(course=course)

    course_comments = CourseComment.objects.filter(is_active=True, course=course)

    course_comments_form = CourseCommentsForm(request.POST or None)

    context = {
        'course': course,
        'season': season,
        'download_api': DOWNLOAD_API,

        'courseComments': course_comments,
        'CommentsForm': course_comments_form,
    }
    if request.user.is_authenticated:
        is_enroll = Enroll.objects.filter(course=course, is_pay=True, is_active=True).first()
        if is_enroll:
            context['access'] = True
            context['enroll'] = is_enroll
        else:
            context['access'] = False

    if course_comments_form.is_valid():
        CourseComment.objects.create(course=course, **course_comments_form.cleaned_data)
        context['send_comment'] = True

    return render(request, 'single_course.html', context)


def download_file(request, episode_pk):
    user = request.user
    episode = Episode.objects.filter(pk=episode_pk).first()

    if not episode.is_free:
        if user.is_authenticated:
            enroll = Enroll.objects.filter(user=user, course=episode.course).first()
            if enroll is None:
                raise Http404('صفحه مورد نظر یافت نشد')
        else:
            messages.error(request,
                           'لطفاٌ برای دانلود فایل ها اول لاگین کنید. ( توجه داشته باشید این قسمت رایگان نیست)')
            redirect(reverse('login'))

    if user.is_authenticated:
        user_download_episode, _ = UserDownloadEpisode.objects.get_or_create(user=user, episode=episode)
        user_download_episode.count += 1
        user_download_episode.save()

    # Define text file name
    filename = episode.path
    # Define the full file path
    if DEBUG:
        filepath = BASE_DIR / 'download-file' / filename
    else:
        filepath = '/home/pytopyir/' + 'download-file/' + filename
    # Open the file for reading content
    try:
        path = open(filepath, 'rb')
    except FileNotFoundError:
        raise Http404('فایل مورد نظر یافت نشد')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type='application/force-download')
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
