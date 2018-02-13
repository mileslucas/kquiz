from django.contrib import admin
from .models import Question, Answer
class QuestionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.dispatcher = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Question, QuestionAdmin);
# Register your models here.
