from django.db import models
from django.db.models.signals import pre_save
from django.db.models import Q
from app_user.models import User

STARS = [
    ('1', 'یک ستاره'),
    ('2', 'دو ستاره'),
    ('3', 'سه ستاره'),
    ('4', 'چهار ستاره'),
    ('5', 'پنج ستاره'),
]
Likes = [
    (True, 'پسندیدن'),
    (False, 'نپسندیدن'),
]


class CourseManager(models.Manager):
    def get_queryset(self):
        return super(CourseManager, self).get_queryset().filter(is_active=True)

    def search(self, query):
        lookup = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(brand__name__icontains=query)
        )
        return self.get_queryset().filter(lookup, is_active=True).distinct()


class Course(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, verbose_name='نام در url')

    name = models.CharField(max_length=150, verbose_name='نام')

    description = models.TextField(verbose_name='توضیحات')

    main_image = models.FileField(upload_to='course/images/main', verbose_name='عکس اصلی', blank=True, null=True)
    alt_image = models.CharField(max_length=100, verbose_name='alt عکس', blank=True, null=True)

    price = models.IntegerField(verbose_name='قیمت')

    discount = models.IntegerField(default=0, verbose_name='تخفیف', blank=True, null=True)

    title_page = models.CharField(max_length=160, verbose_name='عنوان صفحه محصول(برای SEO)')
    description_page = models.CharField(max_length=340, verbose_name='توضیحات صفحه محصول(برای SEO)')

    is_active = models.BooleanField(default=True, verbose_name='موجود/ناموجود')

    objects = models.Manager()
    courses = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/courses/{self.id}/{self.slug}'


def course_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = str(instance.name).replace(" ", "-")


pre_save.connect(course_pre_save_receiver, sender=Course)


class CourseComment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, null=True)

    name = models.CharField(max_length=30)
    email = models.CharField(max_length=80)
    description = models.TextField()
    star = models.CharField(max_length=1, choices=STARS)

    replay = models.ForeignKey('CourseComment', on_delete=models.CASCADE, verbose_name='ریپلای', blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='نمایش/عدم نمایش')


class LikeCourseComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, )
    courseComment = models.ForeignKey(CourseComment, on_delete=models.RESTRICT)

    value = models.BooleanField(choices=Likes)
