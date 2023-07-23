from django.contrib import admin
from .models import Food, Question, Choice

admin.site.register(Food)
admin.site.register(Question)
admin.site.register(Choice)