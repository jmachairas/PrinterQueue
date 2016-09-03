from django.contrib import admin
from .models import User, Printer, Job

admin.site.register(User)
admin.site.register(Printer)
admin.site.register(Job)
