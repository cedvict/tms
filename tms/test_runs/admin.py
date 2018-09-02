from django.contrib import admin

from .models import TestRun, TestRunCase

admin.site.register(TestRun)
admin.site.register(TestRunCase)
