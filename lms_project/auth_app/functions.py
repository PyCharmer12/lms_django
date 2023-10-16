from datetime import datetime
from os.path import splitext

# Создание функции для добавление временной метки к имени загруженного файла (Урок 3).
def get_timestamp_path_user(instance, filename):
    return f'users/{datetime.now().timestamp()}{splitext(filename)[1]}'

