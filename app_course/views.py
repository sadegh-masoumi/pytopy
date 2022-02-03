from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from app_order.models import Enroll
from .models import Season
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
