from django.contrib import admin
from .models import Divorce


# Register models into admin view
@admin.register(Divorce)
class DivorceAdmin(admin.ModelAdmin):
    list_display = ("user", "divorce_status", "date")
    search_fields = ("divorce_status",)
    list_filter = ("date", "divorce_status")


# admin.site.register(Customer)
