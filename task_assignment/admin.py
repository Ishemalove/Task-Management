from django.contrib import admin
from task_assignment.models import Contributor, Task, Attendance

# Register your models here.
admin.site.register(Contributor)
admin.site.register(Task)
admin.site.register(Attendance)