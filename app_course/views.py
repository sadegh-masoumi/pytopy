from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .forms import CourseCommentsForm

from .models import Course, CourseComment, LikeCourseComment


class Courses(ListView):
    template_name = 'all_course.html'
    model = Course


def view_single_course(request, course_id, **kwargs):
    course = get_object_or_404(Course, id=course_id)
    course_comments = CourseComment.objects.filter(is_active=True, course=course)
    course_comments_form = CourseCommentsForm(request.POST or None)

    context = {
        'course': course,
        'courseComments': course_comments,
        'CommentsForm': course_comments_form,
    }

    if course_comments_form.is_valid():
        name = course_comments_form.cleaned_data.get('name')
        email = course_comments_form.cleaned_data.get('email')
        star = course_comments_form.cleaned_data.get('star')
        description = course_comments_form.cleaned_data.get('description')

        CourseComment.objects.create(course=course, name=name, email=email, star=star, description=description)
        context['send_comment'] = True

    return render(request, 'single_course.html', context)
