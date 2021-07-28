from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


# поле PhoneNumberField:
from phonenumber_field.modelfields import PhoneNumberField

# ckeditor:
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.conf import settings
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver





class Sponsor(models.Model):
    """Партнеры"""
    ordernumber = models.IntegerField('Сортировка на сайте')
    name = models.CharField('Название компании', max_length=150)
    image = models.ImageField('Логотип', upload_to='sponsor', blank=True, null=True)
    description = models.TextField('Заметка', blank=True, null=True)
    url = models.URLField('Ссылка', max_length = 300, blank=True, null=True)
    active = models.BooleanField('Активно на сайте', default=False)
    date_joined = models.DateField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["ordernumber"]
        verbose_name = 'партнер'
        verbose_name_plural = "партнеры"

    def admin_logo(self):
        """добавление изображения в админку"""
        if self.image:
            return mark_safe('<img src="%s" style="width: 165px; height:85px;" />' % self.image.url)
        else:
            return "-"
    admin_logo.short_description = 'Изображение'
    admin_logo.allow_tags = True	    

    def clean(self):
        """валидатор изображения"""
        if not self.image:
            raise ValidationError("Нет изображения!")
        else:
            w, h = get_image_dimensions(self.image)
            if w != 165:
                raise ValidationError("Ширина картинки %i px. Должна быть 165 px на 85 px." % w)
            if h != 85:
                raise ValidationError("Высота картинки %i px. Должна быть 165 px на 85 px." % h)



class Schedule(models.Model):
    """Расписание занятий"""
    ordernumber = models.IntegerField('Сортировка на сайте')
    image = models.ImageField('Картинка', upload_to='schedule', blank=True, default='')
    years = models.CharField('Заголовок/года рождения', max_length=150)
    district = models.CharField('Район', max_length=150)
    address = models.CharField('Адрес', max_length=350)
    schedule = models.CharField('Расписание занятий', max_length=350)
    post = models.CharField('Должность', max_length=100)
    contact = models.CharField('ФИО', max_length=350)
    phone = PhoneNumberField('Телефон',)
    active = models.BooleanField('Активно на сайте', default=False)
    # date_joined = models.DateField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.years}, {self.district}'

    class Meta:
        ordering = ["ordernumber"]
        verbose_name = 'расписание тренировок'
        verbose_name_plural = "расписания тренировок"        

    def admin_logo(self):
        """добавление изображения в админку"""
        if self.image:
            return mark_safe('<img src="%s" style="width: 100px; height:150px;" />' % self.image.url)
        else:
            return "-"
    admin_logo.short_description = 'Изображение'
    admin_logo.allow_tags = True



class Feedback(models.Model):
    """Форма обратной связи"""
    name = models.CharField("Имя пользователя", max_length=220)
    email = models.EmailField("Email", max_length=120)
    phone = PhoneNumberField('Телефон', max_length=15)
    text = models.TextField('Текст', null=True,  blank=True)
    date = models.DateTimeField("Дата обращения", default=timezone.now)

    def __str__(self):
        return f'{self.name}, {self.phone}'

    class Meta:
        ordering = ["-date"]
        verbose_name = "форма обратной связи"
        verbose_name_plural = "формы обратной связи"    


class Faq(models.Model):
    """часто задаваемые вопросы"""
    ordernumber = models.IntegerField('Сортировка на сайте')
    title = models.CharField('Заголовок', max_length=300)
    text = models.TextField('Текст', blank=True, null=True)   
    active = models.BooleanField('Активно на сайте', default=False)     

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["ordernumber"]
        verbose_name = 'часто задаваемый вопрос'
        verbose_name_plural = "часто задаваемые вопросы"    


class Coach(models.Model):
    """Тренерский штаб"""
    ordernumber = models.IntegerField('Сортировка на сайте')
    name = models.CharField('ФИО', max_length=250)
    image = models.ImageField('Фото', upload_to='coach', blank=True, null=True)
    post = models.CharField('Должность', max_length=100)
    bith = models.CharField('Дата рождения', max_length=50, blank=True, null=True, 
        help_text="формат заполнения: 10.02.1987 г.")
    instagram = models.URLField('Instagram', max_length = 300, blank=True, null=True,
        help_text="формат заполнения: https://www.instagram.com/")
    facebook = models.URLField('Facebook', max_length = 300, blank=True, null=True,
        help_text="формат заполнения: https://www.instagram.com/")
    twitter = models.URLField('Twitter', max_length = 300, blank=True, null=True,
        help_text="формат заполнения: https://www.instagram.com/")
    active = models.BooleanField('Активно на сайте', default=False)
    date_joined = models.DateField('Дата создания', auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["ordernumber"]
        verbose_name = 'тренер'
        verbose_name_plural = "Тренерский штаб"     

    def admin_logo(self):
        """добавление изображения в админку"""
        if self.image:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image.url)
        else:
            return "-"
    admin_logo.short_description = 'Фото'
    admin_logo.allow_tags = True        

    def clean(self):
        """валидатор изображения"""
        if not self.image:
            raise ValidationError("Нет фото!")
        else:
            w, h = get_image_dimensions(self.image)
            if w != 370:
                raise ValidationError("Ширина картинки %i px. Должна быть 370 px на 370 px." % w)
            if h != 370:
                raise ValidationError("Высота картинки %i px. Должна быть 370 px на 370 px." % h)


class History(models.Model):
    """История клуба"""
    year = models.IntegerField('Год')
    name = models.CharField('Заголовок', max_length=150)
    image = models.ImageField('Картинка', upload_to='history', blank=True, null=True)
    description = models.TextField('Заметка', blank=True, null=True)
    active = models.BooleanField('Активно на сайте', default=False)
    date_joined = models.DateField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["year"]
        verbose_name = 'история клуба'
        verbose_name_plural = "история клуба"    

    def admin_logo(self):
        """добавление изображения в админку"""
        if self.image:
            return mark_safe('<img src="%s" style="width: 150px; height:100px;" />' % self.image.url)
        else:
            return "-"
    admin_logo.short_description = 'Картинка'
    admin_logo.allow_tags = True     


class Post(models.Model):
    """посты блога"""
    title = models.CharField('Заголовок', max_length=250)
    image = models.ImageField('Картинка', upload_to='posts/%Y/%m/%d', blank=True, null=True)
    content_upload = RichTextUploadingField('Статья', blank=True, null=True)
    slug = models.SlugField('Ссылка', max_length=200, unique=True, default='')
    active = models.BooleanField('Активно на сайте', default=False)
    head = models.BooleanField('Разместить в шапке', default=False)
    date_joined = models.DateTimeField('Дата создания', auto_now_add=True)   


    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_joined"]
        verbose_name = 'пост'
        verbose_name_plural = "посты" 

    def get_absolute_url(self):
        """ссылка на экземпляр модели"""
        return reverse('app:detail', kwargs={'slug': self.slug})     


class AttendanceRecord(models.Model):
    """Посещение сайта пользователями"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.PROTECT,)
    login_time = models.DateTimeField('Вход', blank=True, null=True)
    logout_time = models.DateTimeField('Выход', blank=True, null=True)

    def str(self):
        login_dt = timezone.localtime(self.login_time)
        return '{0} - {1.year}/{1.month}/{1.day} {1.hour}:{1.minute}:{1.second} - {2}'.format(
            self.user.username, login_dt, self.get_diff_time()
        )

    class Meta:
        verbose_name = 'посещение сайта пользователями'
        verbose_name_plural = 'посещение сайта пользователями'    

    def get_diff_time(self):
        """Logout time-Login time"""
        if not self.logout_time:
            return 'Not logged out'
        else:
            td = self.logout_time - self.login_time
            return '{0}Time {1} minutes'.format(
                td.seconds // 3600, (td.seconds // 60) % 60)

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    """Called when logging in"""
    AttendanceRecord.objects.create(user=user, login_time=timezone.now())

@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    """Called when you log out"""
    records = AttendanceRecord.objects.filter(user=user, logout_time__isnull=True)
    if records:
        record = records.latest('pk')
        record.logout_time = timezone.now()
        record.save()        

