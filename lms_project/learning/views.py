from django.http import HttpResponse
from django.shortcuts import render
from .models import Course
from datetime import *

# Create your views here.
def index(request):
    courses = Course.objects.all()
    current_year = datetime.now().year
    return render(request, context={'courses': courses, 'current_year': current_year},
                  template_name='index.html')
def create(request):
    return HttpResponse('Здесь будет форма для создания собственного курса')
def delete(request, course_id):
    return HttpResponse(f'Здесь будет производиться удаление {course_id} курса')
def detail(request, course_id):
    return HttpResponse(f'Здесь мы узнаем детальную информацию о {course_id} курсе')
def enroll(request, course_id):
    return HttpResponse(f'Здесь мы сможем записаться на {course_id} курс')

