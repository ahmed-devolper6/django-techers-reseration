from django.contrib import admin
from .models import TeacherProfile , Oder
# Register your models here.
class reportadmin(admin.ModelAdmin):
    list_display = ('name','city', 'subject' , 'tech')
admin.site.register(TeacherProfile , reportadmin)
admin.site.register(Oder)