from django import template
from app_course.models import Course
# from ptp_comments.models import LikeCourseComment

register = template.Library()


def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


def amount(value):
    x = reverse(str(value))
    i = 0
    final = ''
    for char in x:
        if i % 3 == 0:
            final += ','
        final += char
        i += 1
    final = reverse(final[1:])
    return str(final)


register.filter('amount', amount)


def amount_after_discount(product):
    if product.discount is not None:

        price = product.price - int((product.price * (product.discount / 100)))
        return amount(price)
    else:
        return amount(product.price)


register.filter('amount_after_discount', amount_after_discount)


# def like_count(like_comments: LikeCourseComment):
#     return like_comments.filter(value=True).count()
#
#
# def dislike_count(like_comments: LikeCourseComment):
#     return like_comments.filter(value=False).count()
#
#
# register.filter('like_count', like_count)
# register.filter('dislike_count', dislike_count)
