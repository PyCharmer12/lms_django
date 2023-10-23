from django.db import models
from django.conf import settings

# Create your models here.
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

    def __str__(self):
        return f'{self.course.title}: Урок {self.name}'


# Создание модели Tracking с нуля (урок 3).
class Tracking(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT, verbose_name='Урок')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Ученик')
    passed = models.BooleanField(default=None, verbose_name='Пройден?')

    # Перечисление свойств создаваемой модели таблицы Tracking.
    class Meta:
        verbose_name_plural = 'Дневники успеваемости'
        verbose_name = 'Дневник успеваемости'
        ordering = ['-user']

    def __str__(self):
        return f'{self.lesson}: Дневник успеваемости {self.user}'



