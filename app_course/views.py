import mimetypes

from core.settings.base import BASE_DIR

from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from app_order.models import Enroll
from .models import Season, Episode, UserDownloadEpisode
from .forms import CourseCommentsForm

from .models import Course, CourseComment


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

        'courseComments': course_comments,
        'CommentsForm': course_comments_form,
    }
    if request.user.is_authenticated:
        is_enroll = Enroll.objects.filter(course=course, is_pay=True, is_active=True).exists()
        if is_enroll:
            context['access'] = True
        else:
            context['access'] = False

    if course_comments_form.is_valid():
        CourseComment.objects.create(course=course, **course_comments_form.cleaned_data)
        context['send_comment'] = True

    return render(request, 'single_course.html', context)


@login_required(login_url='/login')
def download_file(request, episode_pk):
    user = request.user
    episode = Episode.objects.filter(pk=episode_pk).first()

    user_download_episode, _ = UserDownloadEpisode.objects.get_or_create(user=user, episode=episode)
    user_download_episode.count += 1
    user_download_episode.save()

    # Define text file name
    filename = episode.path
    # Define the full file path
    filepath = BASE_DIR / 'file_download' / 'courses' / filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type='application/force-download')
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
