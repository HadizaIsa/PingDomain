from django.apps import apps
from django.contrib import admin
from django.conf import settings


Domain = apps.get_model(settings.DOMAIN_MODEL)


# Register your models here.
@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain_url', 'created_at', 'updated_at')
    search_fields = ('domain_url',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
