# Импорт классов из библиотеки.
from django.contrib.auth.models import AbstractUser
from django.db import models
from .functions import get_timestamp_path_user



# Create your models here.
# Создание недостающих полей таблицы в модели User на
# основе встроенной модели AbstractUser (урок 3).
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=False)
    description = models.TextField(verbose_name='Обо мне', null=True, blank=True, default='')
    avatar = models.ImageField(verbose_name='Фото', blank=True, upload_to=get_timestamp_path_user)

    # Указание поля для авторизации.
    USERNAME_FIELD = 'email'
    # Указание списка имен полей для создания суперпользователя.
    REQUIRED_FIELDS = ['username']

    #  Перечисление свойств создаваемой модели таблицы.
    class Meta:
        verbose_name_plural = 'Участники'
        verbose_name = 'Участник'
        ordering = ['last_name']

    # Переопределение метода str который позволяет получить информацию о текущем объекте
    def __str__(self):
        return f'Участник {self.first_name} {self.last_name}: {self.email}'






