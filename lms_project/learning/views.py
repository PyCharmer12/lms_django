from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from datetime import *

# Create your views here.
def index(request):
    courses = Course.objects.all()
    current_year = datetime.now().year
    return render(request, context={'courses': courses,
                                    'current_year': current_year
                                    },
                  template_name='index.html')

# Обработчик запроса создания курса :
def create(request):
    if request.method == 'POST':
        data = request.POST
        Course.objects.create(title=data['title'], author=request.user,
                              description=data['description'], start_date=data['start_date'],
                              duration=data['duration'], price=data['price'],
                              count_lessons=data['count_lessons'])
        return redirect('index')
    else:
        return render(request, 'create.html')



# Обработчик запроса удаления курса :
def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('index')


# Обработчик запроса вывода подробной информации о курсе:
def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course_id)
    context = {'course': course, 'lessons': lessons}
    return render(request,'detail.html', context)

# Обработчик запроса записи на курс:
def enroll(request, course_id):
    # Проверка, авторизован ли пользователь:
    if request.user.is_anonymous: # Если не авторизован,
        return redirect('login') # Перенаправить на страницу входа
    else: # Иначе, если пользователь авторизован, то:
        # Проверка - пользователь уже записан на курс?
        is_existed = Tracking.objects.filter(user=request.user).exists()
        if is_existed: # Если записан, то вывод уведомления:
            return HttpResponse(f'Вы уже записаны на данный курс')
        else: # Если не записан, то отобразить уроки конкретного курса:
            lessons = Lesson.objects.filter(course=course_id)
            # И создать набор экземпляров модели Tracking с атрибутами, указанным в models.py,
            records = [Tracking(lesson=lesson, user=request.user, possed=False) for lesson in lessons]
            # Затем создать набор записей в таблице на основе созданного списка records:
            Tracking.objects.bulk_create(records)
            # Выводим уведомление об успешной записи на курс:
            return HttpResponse('Вы записаны на данный курс')


