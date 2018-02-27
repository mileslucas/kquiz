from django.contrib import admin
from .models import Question, Answer
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'completed', 'time_left', 'time_posted', 'dispatcher')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.dispatcher = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
# Register your models here.
