from django.contrib import admin

from .models import Endpoint, CheckLog

admin.site.register(Endpoint)
admin.site.register(CheckLog)
