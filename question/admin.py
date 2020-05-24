from django.contrib import admin
from .models import CategoryLevel1, CategoryLevel2, Question, Options

admin.site.register(CategoryLevel1)
admin.site.register(CategoryLevel2)
admin.site.register(Question)
admin.site.register(Options)
