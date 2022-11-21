from django.contrib import admin
from .models import Teacher, Student, Login, Note, Assignment, TimeTable, Attendance

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Login)
admin.site.register(Note)
admin.site.register(Assignment)
admin.site.register(TimeTable)
admin.site.register(Attendance)