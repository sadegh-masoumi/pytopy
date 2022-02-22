from django.db import models
from django.db.models.signals import pre_save
from django.db.models import Q
from app_user.models import User
from django.urls import reverse

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

    top_description = models.TextField(verbose_name='توضیحات بالای صفحه', blank=True, null=True)
    main_description = models.TextField(verbose_name='توضیحات اصلی', blank=True, null=True)

    price = models.IntegerField(verbose_name='قیمت به تومان')
    time = models.CharField(max_length=10, verbose_name='زمان دوره')

    teacher = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='مدرس')

    main_image = models.FileField(upload_to='course/images/main', verbose_name='عکس اصلی', blank=True, null=True)
    alt_image = models.CharField(max_length=100, verbose_name='alt عکس', blank=True, null=True)

    discount = models.IntegerField(default=0, verbose_name='درصد تخفیف')

    label = models.CharField(null=True, blank=True, max_length=50)

    title_page = models.CharField(max_length=160, verbose_name='عنوان صفحه محصول(برای SEO)')
    description_page = models.CharField(max_length=340, verbose_name='توضیحات صفحه محصول(برای SEO)')

    is_active = models.BooleanField(default=True, verbose_name='موجود/ناموجود')

    objects = models.Manager()
    courses = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('single-curse', kwargs={'pk': self.pk, 'slug': self.slug})

    def get_payment_url(self):
        return reverse('pay-request', kwargs={'course_id': self.pk})

    def get_final_price(self) -> int:
        price = self.price
        if self.discount > 0:
            price = self.price - ((self.discount / 100) * self.price)
        return price

    def get_rial_price(self) -> int:
        return self.get_final_price() * 10


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

    date = models.DateTimeField(auto_now_add=True)
    replay = models.ForeignKey('CourseComment', on_delete=models.CASCADE, verbose_name='ریپلای', blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='نمایش/عدم نمایش')

    def __str__(self):
        return self.name


class LikeCourseComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, )
    courseComment = models.ForeignKey(CourseComment, on_delete=models.RESTRICT)

    value = models.BooleanField(choices=Likes)


class Season(models.Model):
    course = models.ForeignKey(Course, models.CASCADE)
    title = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {self.course}'


class Episode(models.Model):
    title = models.CharField(max_length=100)

    course = models.ForeignKey(Course, models.CASCADE)
    season = models.ForeignKey(Season, models.CASCADE)

    path = models.CharField(max_length=255)
    number = models.IntegerField(auto_created=True)
    time = models.CharField(max_length=10)
    description = models.TextField()

    is_active = models.BooleanField(default=True)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.season}'

    class Meta:
        ordering = ('number',)


class UserDownloadEpisode(models.Model):
    episode = models.ForeignKey(Episode, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.episode}"
