# Импорт классов из библиотеки.
from django.contrib.auth.models import AbstractUser
from django.db import models
from .functions import get_timestamp_path_user
from django.conf import settings


# Create your models here.
# Создание недостающих полей таблицы в модели User на
# основе встроенной модели AbstractUser (урок 3).
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    birthday = models.DateField(verbose_name='Дата рождения', blank=False)
    description = models.TextField(verbose_name='Обо мне', null=True, blank=True, default='')
    avatar = models.ImageField(verbose_name='Фото', blank=True, upload_to=get_timestamp_path_user)

    # Указание поля для авторизации.
    USERNAME_FIELD = 'email'
    # Указание списка имен полей для создания суперпользователя.
    REQUIRED_FIELDS = []

    #  Перечисление свойств создаваемой модели таблицы.
    class Meta:
        verbose_name_plural = 'Участники'
        verbose_name = 'Участник'
        ordering = ['last_name']

    # Переопределение метода str который позволяет получить информацию о текущем объекте
    def __str__(self):
        return f'Участник {self.first_name} {self.last_name}: {self.email}'



# Создание модели Course с нуля (урок 3).
class Course(models.Model):
    title = models.CharField(verbose_name='Название курса', max_length=30, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Автор курса')
    description = models.TextField(verbose_name='Описание курса', max_length=200)
    start_date = models.DateField(verbose_name='Старт курса')
    duration = models.PositiveIntegerField(verbose_name='Продолжительность')
    price = models.PositiveIntegerField(verbose_name='Цена',  blank=True)
    count_lessons = models.PositiveIntegerField(verbose_name='Кол-во уроков')

    #  Перечисление свойств создаваемой модели таблицы Course.
    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'
        ordering = ['title']

    # Переопределение метода str который позволяет
    # получить информацию о текущем объекте
    def __str__(self):
        return f'{self.title}: Старт {self.start_date}'


# Создание модели Lesson с нуля (урок 3).
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    name= models.CharField(verbose_name='Название урока', max_length=25, unique=True)
    preview = models.TextField(verbose_name='Описание урока', max_length=100)

    #  Перечисление свойств создаваемой модели таблицы Lesson.
    class Meta:
        verbose_name_plural = 'Уроки'
        verbose_name = 'Урок'
        ordering = ['course']


# Создание модели Tracking с нуля (урок 3).
class Tracking(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Урок')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Ученик')
    preview = models.BooleanField(default=None, verbose_name='Пройден?')

    # Перечисление свойств создаваемой модели таблицы Tracking.
    class Meta:
        ordering = ['-user']


