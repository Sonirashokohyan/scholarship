from django.contrib import admin
from .models import projects, new

# Register your models here.

class appAdmin(admin.ModelAdmin):
  list_display = ("name", "description",)
admin.site.register(projects, appAdmin,)


class appAdmin_sec(admin.ModelAdmin):
  list_display = ("name", "description",)
admin.site.register(new)
