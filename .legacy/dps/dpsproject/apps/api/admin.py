from django.contrib import admin
from .models import DPS

# admin.site.register(DPS)


@admin.register(DPS)
class DPSAdmin(admin.ModelAdmin):
    list_display = ("user", "divorce_status", "date")
    search_fields = ("divorce_status",)
    list_filter = ("divorce_status", "date")
