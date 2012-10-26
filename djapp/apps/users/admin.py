from django.contrib import admin
from django.contrib.admin import ModelAdmin
from djapp.apps.users.models import petition


admin.site.register(petition)

