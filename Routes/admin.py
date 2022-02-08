from django.contrib import admin
from .models import CircuitData
from import_export.admin import ImportExportModelAdmin

admin.site.register(CircuitData,ImportExportModelAdmin)
