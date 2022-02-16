from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(CircuitData,ImportExportModelAdmin)
admin.site.register(TransformerData,ImportExportModelAdmin)
admin.site.register(LoadData,ImportExportModelAdmin)
admin.site.register(phFaultData,ImportExportModelAdmin)
admin.site.register(earthFaultData,ImportExportModelAdmin)
admin.site.register(Generation,ImportExportModelAdmin)
admin.site.register(InterestConnections,ImportExportModelAdmin)
admin.site.register(OppRestrictions,ImportExportModelAdmin)
admin.site.register(FaultData,ImportExportModelAdmin)