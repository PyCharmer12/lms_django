from django.contrib import admin
from .models import Course, Lesson


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'start_date',)
    exclude = ('description', 'duration', 'price',)
    search_fields = ('title', 'start_date', 'description', )
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True
    action_selection_counter = True
    save_on_top = True
    list_display_links = ('title', 'start_date',)
    list_editable = ('author', )
    pass

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


