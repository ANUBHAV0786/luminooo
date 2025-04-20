from django.contrib import admin

from . import models
# we will Register our models here.
admin.site.register(models.Teacher)
admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.Student)



# Register your models here.
