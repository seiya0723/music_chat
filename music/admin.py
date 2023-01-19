from django.contrib import admin
from .models import instrument,Teacher, language, teacher_picture
admin.site.register(instrument)
admin.site.register(language)
admin.site.register(Teacher)
admin.site.register(teacher_picture)

# Register your models here.