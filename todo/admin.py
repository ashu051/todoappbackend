from django.contrib import admin

# Register your models here.
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','name')
admin.site.register(Todo,TodoAdmin)